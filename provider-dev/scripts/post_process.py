import os
import sys
import re

services_dir = sys.argv[1]

# Process all yaml files first for common replacements
for filename in os.listdir(services_dir):
    if not filename.endswith('.yaml'):
        continue
    
    file_path = os.path.join(services_dir, filename)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Common replacements for all files
    if './common.yaml' in content or 'common.yaml' in content:
        content = content.replace('./common.yaml', "'").replace('common.yaml', "'")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Replaced common.yaml references in: {filename}")

# Special processing for cortex-inference.yaml
cortex_file_path = os.path.join(services_dir, 'cortex-inference.yaml')
if os.path.exists(cortex_file_path):
    with open(cortex_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add the Any schema to components/schemas
    if 'components:' in content and 'schemas:' in content:
        # Find where to insert the Any schema
        schemas_pattern = re.compile(r'(components:\s*\n\s*schemas:\s*\n)', re.MULTILINE)
        match = schemas_pattern.search(content)
        
        if match:
            any_schema = """    Any:
      description: Generic schema that accepts any value
      nullable: true
      additionalProperties: true
"""
            # Insert the Any schema after the schemas section start
            content = content[:match.end()] + any_schema + content[match.end():]
            print("✅ Added Any schema to components/schemas")
    
    # 2. Replace all references to common-cortex-tool.yaml
    pattern = r'common-cortex-tool\.yaml#/components/schemas/[a-zA-Z0-9]+'
    replacements = 0
    
    for match in re.finditer(pattern, content):
        content = content.replace(match.group(0), '#/components/schemas/Any')
        replacements += 1
        
    content = content.replace('#/components/schemas/Any', "'#/components/schemas/Any'")
    
    print(f"✅ Replaced {replacements} references to common-cortex-tool.yaml schemas")
    
    # Write the changes back to the file
    with open(cortex_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Updated cortex-inference.yaml")
else:
    print("⚠️ cortex-inference.yaml not found in the specified directory")

print("✅ All processing completed")