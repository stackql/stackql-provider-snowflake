# openapi_to_stackql/convert.py

import os
import csv
import yaml
import json
from collections import defaultdict
from typing import Dict, Any


def load_manifest(config_path: str) -> Dict[str, Dict[str, str]]:
    manifest = {}
    with open(config_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = f"{row['filename']}::{row['operationId']}"
            manifest[key] = row
    return manifest


def load_spec(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        if filepath.endswith(".json"):
            return json.load(f)
        return yaml.safe_load(f)


def write_spec(filepath: str, data: Dict[str, Any]):
    with open(filepath, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False)


def encode_ref_path(path: str, verb: str) -> str:
    encoded_path = path.replace('/', '~1')
    return f"#/paths/{encoded_path}/{verb}"


def get_success_response_info(operation: Dict[str, Any]) -> Dict[str, str]:
    responses = operation.get("responses", {})
    two_xx_codes = sorted([code for code in responses if code.startswith("2")])

    if not two_xx_codes:
        return {"mediaType": "", "openAPIDocKey": ""}

    lowest_2xx = two_xx_codes[0]
    content = responses.get(lowest_2xx, {}).get("content", {})
    media_types = list(content.keys())

    media_type = media_types[0] if media_types else ""

    return {
        "mediaType": media_type,
        "openAPIDocKey": lowest_2xx
    }


def snake_case(name: str) -> str:
    return name.replace("-", "_")


def run(input_dir: str, output_dir: str, config_path: str, provider_id: str, servers: str = None, provider_config: str = None, skip_files: list[str] = []):
    version = "v00.00.00000"
    services_path = os.path.join(output_dir, version, "services")
    os.makedirs(services_path, exist_ok=True)

    # Clean all files in services output dir
    for file in os.listdir(services_path):
        file_path = os.path.join(services_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print(f"🧹 Cleared all files in {services_path}")

    # delete provider.yaml file
    provider_manifest_file = os.path.join(output_dir, version, "provider.yaml")
    if os.path.isfile(provider_manifest_file):
        os.remove(provider_manifest_file)
    print(f"🧹 Deleted {provider_manifest_file}")

    manifest = load_manifest(config_path)

    provider_services = {}

    for filename in os.listdir(input_dir):
        if filename in skip_files:
            print(f"⏭️  Skipping {filename} (matched --skip)")
            continue

        if not filename.endswith((".yaml", ".yml", ".json")):
            continue

        base_name = os.path.splitext(filename)[0]
        service_name = snake_case(base_name)

        spec_path = os.path.join(input_dir, filename)
        spec = load_spec(spec_path)

        resources = defaultdict(lambda: {
            "methods": {},
            "sqlVerbs": {"select": [], "insert": [], "update": [], "delete": [], "replace": []}
        })

        for path, path_item in spec.get("paths", {}).items():
            for verb, operation in path_item.items():
                if not isinstance(operation, dict):
                    continue

                operation_id = operation.get("operationId")
                if not operation_id:
                    continue

                manifest_key = f"{filename}::{operation_id}"
                entry = manifest.get(manifest_key)
                if not entry:
                    print(f"❌ ERROR: {filename} → {operation_id} not found in manifest")
                    raise SystemExit(1)

                resource = entry["stackql_resource_name"]
                method = entry["stackql_method_name"]
                sqlverb = entry["stackql_verb"]

                path_ref = encode_ref_path(path, verb)
                response_info = get_success_response_info(operation)

                method_entry = {
                    "operation": {"$ref": path_ref},
                    "response": response_info
                }

                resources[resource]["id"] =f"{provider_id}.{service_name}.{resource}" 
                resources[resource]["name"] = resource
                resources[resource]["title"] = resource.replace("_", " ").title()
                resources[resource]["methods"][method] = method_entry
                if sqlverb:
                    resources[resource]["sqlVerbs"][sqlverb].append({
                        "$ref": f"#/components/x-stackQL-resources/{resource}/methods/{method}"
                    })

        # Inject into spec
        if "components" not in spec:
            spec["components"] = {}
        spec["components"]["x-stackQL-resources"] = dict(resources)

        # Inject servers if provided
        if servers:
            try:
                servers_json = json.loads(servers)
                spec["servers"] = servers_json
            except json.JSONDecodeError as e:
                print(f"❌ Failed to parse servers JSON: {e}")
                raise SystemExit(1)

        # Write enriched spec
        output_path = os.path.join(services_path, filename)
        write_spec(output_path, spec)
        print(f"✅ Wrote enriched spec: {output_path}")

        # Add providerService entry
        info = spec.get("info", {})
        spec_title = info.get("title", f"{service_name.replace('_', ' ').title()} API")
        spec_description = info.get("description", f"TODO: add description for {service_name}")

        provider_services[service_name] = {
            "id": f"{service_name}:{version}",
            "name": service_name,
            "preferred": True,
            "service": {
                "$ref": f"{provider_id}/{version}/services/{filename}"
            },
            "title": spec_title,
            "version": version,
            "description": spec_description
        }

    # Write provider.yaml
    provider_yaml = {
        "id": provider_id,
        "name": provider_id,
        "version": version,
        "providerServices": provider_services,
    }

    if provider_config:
        try:
            provider_config_json = json.loads(provider_config)
            provider_yaml["config"] = provider_config_json
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse provider config JSON: {e}")
            raise SystemExit(1)

    write_spec(os.path.join(output_dir, version, "provider.yaml"), provider_yaml)
    print(f"📦 Wrote provider.yaml to {output_dir}/{version}/provider.yaml")
