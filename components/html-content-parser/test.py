import json                    
from parser import parse_html 
import sys

def main() -> None:
    """Entry point for the commandline helper.

    Expected usage:
        python test.py <path_to_html_file>

    The script reads the HTML file, runs ``parse_html`` on its contents,
    and prints the resulting Python dictionary as nicely-indented JSON.
    """
    if len(sys.argv) < 2:
        print("Usage: python test.py <path_to_html_file>")
        sys.exit(1)

    document_path = sys.argv[1]

    with open(document_path, "r", encoding="utf-8") as f:
        html = f.read()

    parsed = parse_html(html)

    print(json.dumps(parsed, indent=2))

if __name__ == "__main__":
    main()