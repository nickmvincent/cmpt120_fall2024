import re
import sys
import os

def extract_python_code(slidev_md_file, output_py_file):
    with open(slidev_md_file, 'r') as f:
        content = f.read()

    # Regex pattern to extract Python code blocks
    python_blocks = re.findall(r'```python\n(.*?)\n```', content, re.DOTALL)

    # Write the extracted Python code to the output file
    with open(output_py_file, 'w') as f:
        for block in python_blocks:
            f.write(block + '\n\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <slidev_md_file>")
    else:
        slidev_md_file = sys.argv[1]
        base_name = os.path.splitext(slidev_md_file)[0]
        output_py_file = f"{base_name}_code.py"

        extract_python_code(slidev_md_file, output_py_file)
        print(f"Python code extracted to {output_py_file}")
