# Gets code from slidev .md file and puts it into python .py file

import re

def extract_python_code(slidev_md_file, output_py_file):
    with open(slidev_md_file, 'r') as f:
        content = f.read()

    # Regex pattern to extract Python code blocks
    python_blocks = re.findall(r'```python\n(.*?)\n```', content, re.DOTALL)

    # Write the extracted Python code to the output file
    with open(output_py_file, 'w') as f:
        for block in python_blocks:
            f.write(block + '\n\n')

# Example usage
slidev_md_file = 'slides.md'
output_py_file = 'extracted_code.py'

extract_python_code(slidev_md_file, output_py_file)
