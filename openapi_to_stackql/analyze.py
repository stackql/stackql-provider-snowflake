# openapi_to_stackql/analyze.py

import os, json, yaml, csv
from typing import Dict, Any

def load_spec(filepath: str) -> Dict[str, Any]:
    with open(filepath, 'r') as f:
        if filepath.endswith(".json"):
            return json.load(f)
        return yaml.safe_load(f)

def extract_main_2xx_response(response_obj: Dict[str, Any]) -> str:
    for code, response in response_obj.items():
        if str(code).startswith("2"):
            content = response.get("content", {})
            app_json = content.get("application/json", {})
            schema = app_json.get("schema", {})

            # Case 1: Direct $ref
            if "$ref" in schema:
                return schema["$ref"].split("/")[-1]

            # Case 2: Array of items
            if schema.get("type") == "array":
                items = schema.get("items", {})
                if "$ref" in items:
                    return items["$ref"].split("/")[-1]
    return ""

def run(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "all_services.csv")

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "path", "operationId", "verb", "response_object", "tags", "stackql_resource_name", "stackql_method_name", "stackql_verb"])

        for filename in os.listdir(input_dir):
            if not filename.endswith((".yaml", ".yml", ".json")):
                continue

            filepath = os.path.join(input_dir, filename)
            spec = load_spec(filepath)

            for path, path_item in spec.get("paths", {}).items():
                for verb, operation in path_item.items():
                    if not isinstance(operation, dict):
                        continue

                    operation_id = operation.get("operationId", "")
                    response_obj = operation.get("responses", {})
                    response_ref = extract_main_2xx_response(response_obj)
                    tags_list = operation.get("tags", [])
                    tags_str = "|".join(tags_list) if tags_list else ""

                    writer.writerow([filename, path, operation_id, verb, response_ref, tags_str, "", "", ""])
