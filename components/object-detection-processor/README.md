# Object Detection Processor

## Purpose 
Object detection using MediaPipe.

## Technologies
Python, MediaPipe, OpenCV.

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
from detect_objects import detect_objects

image_path = "synthetic_data/sample.jpg"
# Detect objects in the image and print results
detect_objects(image_path)
```

### Command‑line usage

```bash
python test.py synthetic_data/sample.jpg
```
