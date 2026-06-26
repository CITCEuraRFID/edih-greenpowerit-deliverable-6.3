# QR Code Reader

## Purpose
Read QR codes from images.

## Technologies
Python, pyzbar, Pillow

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

The component can be used programmatically as shown below **or** through its command‑line helper.

### Programmatic usage

```python
from qr_code_reader import read_qr_code

data = read_qr_code("path/to/image.png")
print(data)
```

### Command‑line usage

```bash
python test.py path/to/image.png
```