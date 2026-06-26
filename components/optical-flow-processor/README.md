# Optical Flow Processor

## Purpose  
Provides a standalone implementation for computing optical flow between consecutive images. Useful for motion analysis, video frame interpolation, and activity detection.

## Technologies  
Python, OpenCV, NumPy  

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

The component can be used programmatically **or** via its small command‑line helper `test.py`.

### Programmatic usage

```python
from optical_flow_processor import OpticalFlowProcessor
import cv2

# Load two images as grayscale (required by the processor)
img1 = cv2.imread("data/frame1.jpeg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("data/frame2.jpeg", cv2.IMREAD_GRAYSCALE)

processor = OpticalFlowProcessor()
flow = processor.compute_flow(img1, img2)

print("Flow shape:", flow.shape)
```

### Command‑line usage

```bash
python test.py data/frame1.jpeg data/frame2.jpeg
```

The script reads the two image files, computes dense optical flow with
`OpticalFlowProcessor`, prints a short summary and optionally writes a visualisation
(`flow.jpeg`) to the current directory.

> **Note:** Place two sample images (e.g. `frame1.jpeg` and `frame2.jpeg`) in the `data/` directory before running the script.