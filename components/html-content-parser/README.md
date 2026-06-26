# html-content-parser

## Purpose
Parse HTML content and convert to structured JSON.

## Technologies
Python, BeautifulSoup

## Installation 
Create a virtual environment in the project folder

```bash
python -m venv .venv

# Activate the environment
# macOS / Linux
source .venv/bin/activate
# Windows (cmd)
.venv\Scripts\activate.bat
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```
Install required libraries
```bash
# (Optional) Upgrade pip inside the venv
python -m pip install --upgrade pip

pip install -r requirements.txt
```

## Usage

The component can be used programmatically as shown below **or** through its command‑line helper `test.py`.

### Programmatic usage

```python
from html_content_parser.parser import parse_html

html = """<html><body><h1>Hello</h1><p>World</p></body></html>"""
result = parse_html(html)
print(result)
```

### Command‑line usage

```bash
# After installing dependencies in a virtual environment
python test.py sample.html
```

The script reads the specified HTML file, parses it using `parse_html`, and prints the resulting JSON:

```json
{
  "title": "Sample Page",
  "body": "Sample Page Welcome This is a sample HTML page for testing the parser. It contains multiple paragraphs and some bold text."
}
```

The component includes synthetic sample data (`sample.html`) and a simple parser implementation.