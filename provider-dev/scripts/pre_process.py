#!/usr/bin/env python3

import os
import yaml
import sys
import copy

def load_yaml(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def write_yaml(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False)

def merge_components(target, common):
    if "components" not in target:
        target["components"] = {}

    for section, items in common.get("components", {}).items():
        if section == "securitySchemes":
            # Replace the entire securitySchemes section
            target["components"][section] = copy.deepcopy(items)
        elif section not in target["components"]:
            target["components"][section] = copy.deepcopy(items)
        else:
            for key, value in items.items():
                if key not in target["components"][section]:
                    target["components"][section][key] = copy.deepcopy(value)

def run(input_dir, keywords_to_rename=None):
    # Default keywords to rename if none provided
    if keywords_to_rename is None:
        keywords_to_rename = {
            "database": "database_name",
            "schema": "schema_name",
            "table": "table_name",
            "view": "view_name",
            "function": "function_name",
            "procedure": "procedure_name",
            "stage": "stage_name",
            "pipe": "pipe_name",
            "task": "task_name",
            "stream": "stream_name"
        }
    
    common_path = os.path.join(input_dir, "common.yaml")
    if not os.path.isfile(common_path):
        print(f"❌ common.yaml not found in {input_dir}")
        sys.exit(1)
    
    common_spec = load_yaml(common_path)
    
    # First, modify the common.yaml file to rename reserved words in parameters
    if 'components' in common_spec and 'parameters' in common_spec['components']:
        renamed_params = {}
        for param_name, param_def in common_spec['components']['parameters'].items():
            if param_name in keywords_to_rename:
                new_param_name = keywords_to_rename[param_name]
                # Make a copy of the parameter definition
                param_def_copy = copy.deepcopy(param_def)
                # Update the name field inside the parameter definition
                param_def_copy['name'] = new_param_name
                renamed_params[new_param_name] = param_def_copy
            else:
                renamed_params[param_name] = param_def
        
        # Replace the original parameters with renamed ones
        common_spec['components']['parameters'] = renamed_params
        
        # Write the updated common.yaml back
        write_yaml(common_path, common_spec)
        print(f"🔧 Updated parameters in common.yaml")
    
    # Now process all YAML files to update path parameters and references
    for filename in os.listdir(input_dir):
        if not filename.endswith((".yaml", ".yml")) or filename == "common.yaml":
            continue
        
        input_full_path = os.path.join(input_dir, filename)
        
        print(f"🔧 Processing: {filename}")
        spec = load_yaml(input_full_path)
        
        # Merge components as in the original script
        merge_components(spec, common_spec)
        
        # Rename path parameters in URL paths
        if 'paths' in spec:
            updated_paths = {}
            for path, path_item in spec['paths'].items():
                new_path = path
                for keyword, replacement in keywords_to_rename.items():
                    # Replace {keyword} with {replacement} in path
                    new_path = new_path.replace(f"{{{keyword}}}", f"{{{replacement}}}")
                
                # If the path was updated, we need to update the parameter references
                if new_path != path:
                    # Deep copy the path item to avoid modifying it while iterating
                    path_item_copy = copy.deepcopy(path_item)
                    for method, operation in path_item_copy.items():
                        if method in ["get", "post", "put", "delete", "patch"] and "parameters" in operation:
                            # Update parameter references
                            updated_params = []
                            for param in operation["parameters"]:
                                if isinstance(param, dict) and "name" in param:
                                    if param["name"] in keywords_to_rename:
                                        param["name"] = keywords_to_rename[param["name"]]
                                    updated_params.append(param)
                                elif "$ref" in param:
                                    # Handle $ref to parameters
                                    ref_path = param["$ref"]
                                    for keyword, replacement in keywords_to_rename.items():
                                        if f"parameters/{keyword}" in ref_path:
                                            param["$ref"] = ref_path.replace(f"parameters/{keyword}", f"parameters/{replacement}")
                                    updated_params.append(param)
                                else:
                                    updated_params.append(param)
                            
                            operation["parameters"] = updated_params
                    
                    updated_paths[new_path] = path_item_copy
                else:
                    updated_paths[path] = path_item
            
            # Replace the original paths with updated ones
            spec['paths'] = updated_paths
        
        # Write the updated spec back to the file
        write_yaml(input_full_path, spec)
    
    print("✅ Done.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pre_process.py <input_dir>")
        sys.exit(1)

    run(sys.argv[1])
