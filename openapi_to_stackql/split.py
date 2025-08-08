# openapi_to_stackql/split.py

import yaml
import json
import os
import re
import logging
from typing import Dict, List, Any, Set, Optional

# Constants
# PROVIDER_VERSION = "v1"
OPERATIONS = ["get", "post", "put", "delete", "patch", "options", "head", "trace"]
NON_OPERATIONS = ["parameters", "servers", "summary", "description"]
COMPONENTS_CHILDREN = ["schemas", "responses", "parameters", "examples", "requestBodies", "headers", "securitySchemes", "links", "callbacks"]

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def create_dest_dir(dest_dir: str, overwrite: bool) -> bool:
    """Create destination directory."""
    if os.path.exists(dest_dir):
        if not overwrite:
            logger.error(f"Destination directory {dest_dir} already exists. Use --overwrite to force.")
            return False
    os.makedirs(dest_dir, exist_ok=True)
    # os.makedirs(os.path.join(dest_dir, "services"), exist_ok=True)
    return True

def is_operation_excluded(exclude: List[str], op_item: Dict, svc_discriminator: str) -> bool:
    """Check if operation should be excluded."""
    if not exclude:
        return False
        
    # Example: exclude based on tags or other criteria
    if 'tags' in op_item and any(tag in exclude for tag in op_item['tags']):
        return True
        
    return False

def ret_service_name_and_desc(provider_name: str, op_item: Dict, path_key: str, 
                              svc_discriminator: str, all_tags: List[Dict], debug: bool) -> tuple[str, str]:
    """Determine service name and description using discriminator."""
    service = "default"
    service_desc = f"{provider_name} API"
    
    # Use tags if discriminator is "tag"
    if svc_discriminator == "tag" and 'tags' in op_item and op_item['tags']:
        service = op_item['tags'][0].lower().replace('-', '_').replace(' ', '_')
        
        # Find description in all_tags
        for tag in all_tags:
            if tag.get('name') == service:
                service_desc = tag.get('description', service_desc)
                break
    
    # Use first path segment if discriminator is "path"
    elif svc_discriminator == "path":
        path_parts = path_key.strip('/').split('/')
        if path_parts:
            service = path_parts[0].lower().replace('-', '_').replace(' ', '_')
            service_desc = f"{provider_name} {service} API"
    
    # Check if service should be skipped
    if service in ["skip"]:
        return "skip", ""
        
    return service, service_desc

def init_service(services: Dict, components_children: List[str], service: str, 
                 service_desc: str, api_doc: Dict) -> Dict:
    """Initialize service map."""
    services[service] = {
        "openapi": api_doc.get("openapi", "3.0.0"),
        "info": {
            "title": f"{service} API",
            "description": service_desc,
            "version": api_doc.get("info", {}).get("version", "1.0.0")
        },
        "paths": {},
        "components": {}
    }
    
    # Initialize components sections
    services[service]["components"] = {child: {} for child in components_children}
    
    # Copy servers if present
    if "servers" in api_doc:
        services[service]["servers"] = api_doc["servers"]
        
    return services

def get_all_refs(obj: Any) -> Set[str]:
    """Extract all $ref values from an object recursively."""
    refs = set()
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "$ref" and isinstance(value, str):
                refs.add(value)
            elif isinstance(value, (dict, list)):
                refs.update(get_all_refs(value))
    elif isinstance(obj, list):
        for item in obj:
            refs.update(get_all_refs(item))
            
    return refs

def add_refs_to_components(refs: Set[str], service: Dict, components: Dict, debug: bool) -> None:
    """Add referenced components to service."""
    for ref in refs:
        parts = ref.split('/')
        
        # Only process refs that point to components
        if len(parts) >= 4 and parts[1] == "components":
            component_type = parts[2]
            component_name = parts[3]
            
            # Check if component type exists in service
            if component_type not in service["components"]:
                service["components"][component_type] = {}
                
            # Skip if component already added
            if component_name in service["components"][component_type]:
                continue
                
            # Add component if it exists in source document
            if (component_type in components and 
                component_name in components[component_type]):
                service["components"][component_type][component_name] = components[component_type][component_name]
                if debug:
                    logger.debug(f"Added component {component_type}/{component_name}")

def add_missing_object_types(obj: Any) -> Any:
    """Add missing type: object to schema objects."""
    if isinstance(obj, dict):
        # If it has properties but no type, add type: object
        if "properties" in obj and "type" not in obj:
            obj["type"] = "object"
            
        # Process nested objects
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                obj[key] = add_missing_object_types(value)
    elif isinstance(obj, list):
        return [add_missing_object_types(item) for item in obj]
        
    return obj

def run(api_doc: str, provider_name: str, output: str, 
        svc_discriminator: str = "tag", exclude: Optional[str] = None, 
        overwrite: bool = False, verbose: bool = False) -> bool:
    """Split OpenAPI document into service-specific files."""

    # Rename output to output_dir for internal consistency
    output_dir = output
    
    # Setup logging based on verbosity
    if verbose:
        logger.setLevel(logging.DEBUG)
    
    logger.info(f"🔄 Splitting OpenAPI doc for {provider_name}")
    logger.info(f"API Doc: {api_doc}")
    logger.info(f"Output: {output_dir}")
    logger.info(f"Service Discriminator: {svc_discriminator}")
    
    # Process exclude list
    exclude_list = exclude.split(",") if exclude else []
    
    # Read the OpenAPI document
    try:
        with open(api_doc, 'r', encoding='utf-8') as f:
            api_doc_obj = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"❌ Failed to parse {api_doc}: {str(e)}")
        return False
    
    # Create destination directory
    # dest_dir = os.path.join(output_dir, provider_name, PROVIDER_VERSION)
    if not create_dest_dir(output_dir, overwrite):
        return False
    
    # Get API paths
    api_paths = api_doc_obj.get('paths', {})
    logger.info(f"📑 Iterating over {len(api_paths)} paths")
    
    services = {}
    op_counter = 0
    
    # Process each path
    for path_key, path_item in api_paths.items():
        if verbose:
            logger.debug(f"Processing path {path_key}")
        
        if not path_item:
            continue
            
        # Process each operation (HTTP verb)
        for verb_key, op_item in path_item.items():
            if verb_key not in OPERATIONS or not op_item:
                continue
                
            op_counter += 1
            if op_counter % 100 == 0:
                logger.info(f"⚙️ Operations processed: {op_counter}")
            
            if verbose:
                logger.debug(f"Processing operation {path_key}:{verb_key}")
                
            # Skip excluded operations
            if is_operation_excluded(exclude_list, op_item, svc_discriminator):
                continue
                
            # Determine service name
            service, service_desc = ret_service_name_and_desc(
                provider_name, op_item, path_key, svc_discriminator, 
                api_doc_obj.get('tags', []), verbose
            )
            
            # Skip if service is marked to skip
            if service == 'skip':
                logger.warning(f"⏭️ Skipping service: {service}")
                continue
                
            if verbose:
                logger.debug(f"Service name: {service}")
                logger.debug(f"Service desc: {service_desc}")
                
            # Initialize service if first occurrence
            if service not in services:
                if verbose:
                    logger.debug(f"First occurrence of {service}")
                services = init_service(services, COMPONENTS_CHILDREN, service, service_desc, api_doc_obj)
                
            # Add operation to service
            if path_key not in services[service]['paths']:
                if verbose:
                    logger.debug(f"First occurrence of {path_key}")
                services[service]['paths'][path_key] = {}
                
            services[service]['paths'][path_key][verb_key] = op_item
            
            # Special case for GitHub
            if (provider_name == 'github' and 
                'x-github' in op_item and 
                'subcategory' in op_item['x-github']):
                services[service]['paths'][path_key][verb_key]['x-stackQL-resource'] = camel_to_snake(
                    op_item['x-github']['subcategory']
                )
                
            # Get all refs for operation
            op_refs = get_all_refs(op_item)
            
            if verbose:
                logger.debug(f"Found {len(op_refs)} refs for {service}")
                
            # Add refs to components
            add_refs_to_components(op_refs, services[service], api_doc_obj.get('components', {}), verbose)
            
            # Get internal refs
            for _ in range(3):  # Internal ref depth
                int_refs = get_all_refs(services[service]['components'])
                if verbose:
                    logger.debug(f"Found {len(int_refs)} INTERNAL refs for service {service}")
                add_refs_to_components(int_refs, services[service], api_doc_obj.get('components', {}), verbose)
                
            # Get deeply nested schema refs
            for _ in range(10):  # Schema max ref depth
                int_refs = get_all_refs(services[service]['components'])
                # Filter refs that are already in service components
                filtered_refs = set()
                for ref in int_refs:
                    parts = ref.split('/')
                    if (len(parts) >= 4 and parts[1] == "components" and parts[2] == "schemas" and
                        parts[3] not in services[service]['components']['schemas']):
                        filtered_refs.add(ref)
                        
                if verbose:
                    logger.debug(f"Found {len(filtered_refs)} INTERNAL schema refs for service {service}")
                    
                if filtered_refs:
                    if verbose:
                        logger.debug(f"Adding {len(filtered_refs)} INTERNAL schema refs for service {service}")
                    add_refs_to_components(filtered_refs, services[service], api_doc_obj.get('components', {}), verbose)
                else:
                    if verbose:
                        logger.debug(f"Exiting INTERNAL schema refs for {service}")
                    break
    
    # Add non-operations to each service
    for service in services:
        for path_key in list(services[service]['paths'].keys()):
            if verbose:
                logger.debug(f"Adding non operations to {service} for path {path_key}")
                
            for non_op in NON_OPERATIONS:
                if verbose:
                    logger.debug(f"Looking for non operation {non_op} in {service} under path {path_key}")
                    
                if path_key in api_paths and non_op in api_paths[path_key]:
                    if verbose:
                        logger.debug(f"Adding {non_op} to {service} for path {path_key}")
                        
                    # Special case for parameters
                    if non_op == 'parameters':
                        for verb_key in services[service]['paths'][path_key]:
                            services[service]['paths'][path_key][verb_key]['parameters'] = api_paths[path_key]['parameters']
    
    # Update path param names (replace hyphens with underscores)
    for service in services:
        if 'paths' in services[service]:
            path_keys = list(services[service]['paths'].keys())
            for path_key in path_keys:
                if verbose:
                    logger.debug(f"Renaming path params in {service} for path {path_key}")
                
                # Replace hyphens with underscores in path parameters
                updated_path_key = re.sub(r'(?<=\{)([^}]+?)-([^}]+?)(?=\})', r'\1_\2', path_key)
                
                if updated_path_key != path_key:
                    if verbose:
                        logger.debug(f"Updated path key from {path_key} to {updated_path_key}")
                    
                    services[service]['paths'][updated_path_key] = services[service]['paths'][path_key]
                    del services[service]['paths'][path_key]
                    
                    # Also update parameter names in operations
                    for verb_key in services[service]['paths'][updated_path_key]:
                        operation = services[service]['paths'][updated_path_key][verb_key]
                        if 'parameters' in operation:
                            for param in operation['parameters']:
                                if param.get('in') == 'path' and '-' in param.get('name', ''):
                                    original_name = param['name']
                                    param['name'] = param['name'].replace('-', '_')
                                    if verbose:
                                        logger.debug(f"Updated parameter name from {original_name} to {param['name']} in path {updated_path_key}")
    
    # Fix missing type: object
    for service in services:
        if verbose:
            logger.debug(f"Updating paths for {service}")
        services[service]['paths'] = add_missing_object_types(services[service]['paths'])
        services[service]['components'] = add_missing_object_types(services[service]['components'])
    
    # Write out service docs
    for service in services:
        logger.info(f"✅ Writing out OpenAPI doc for [{service}]")
        # svc_dir = os.path.join(output_dir, provider_name, PROVIDER_VERSION, 'services', service)
        svc_dir = os.path.join(output_dir, service)
        output_file = os.path.join(svc_dir, f"{service}.yaml")
        
        os.makedirs(svc_dir, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(services[service], f, default_flow_style=False)
    
    logger.info(f"🎉 Successfully split OpenAPI doc into {len(services)} services")
    return True