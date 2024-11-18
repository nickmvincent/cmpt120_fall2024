import re

def extract_details(input_file, output_file):
    with open(input_file, 'r') as infile:
        content = infile.read()

    details_content = re.findall(r'<details>(.*?)</details>', content, re.DOTALL)

    with open(output_file, 'w') as outfile:
        for detail in details_content:
            # Remove <summary> tags and replace with a header
            detail = re.sub(r'<summary>(.*?)</summary>', r'## \1', detail)
            outfile.write(detail.strip() + "\n\n")

# Usage
extract_details('readings.md', 'outcomes.md')
