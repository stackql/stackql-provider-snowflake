import os
import re
import sys

services_dir = sys.argv[1]

#
# Process all yaml files first for common replacements
#
for filename in os.listdir(services_dir):
    if not filename.endswith('.yaml'):
        continue
    
    file_path = os.path.join(services_dir, filename)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Common replacements for all files
    if './common.yaml' in content or 'common.yaml' in content:
        content = content.replace('./common.yaml', '').replace('common.yaml', '')

    # hack for this non existent file
    if filename == "cortex-inference.yaml":
        content = re.sub(r'common-cortex-tool\.yaml#/components/schemas/(\w+)', r"'#/components/schemas/\1'", content)        
        # pattern = r'common-cortex-tool\.yaml#/components/schemas/\w+'
        # matches = re.findall(pattern, content)
    
        # if matches:
        #     print(f"\n=== MATCHES IN {filename} ===")
        #     for match in matches:
        #         print(f"Found: {match}")
        # else:
        #     print(f"No matches found in {filename}")


    lines = content.split('\n')
    for i in range(len(lines)):
        # Find all unquoted $ref entries and quote them (without escaping)
        if '$ref: #' in lines[i] and not ('$ref: \'#' in lines[i] or '$ref: "#' in lines[i]):
            ref_part = lines[i].split('$ref: ')[1]
            lines[i] = lines[i].replace('$ref: ' + ref_part, '$ref: \'' + ref_part + '\'')

    content = '\n'.join(lines)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Replaced common.yaml references in: {filename}")

print("✅ All processing completed")