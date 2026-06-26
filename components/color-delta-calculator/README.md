# Color Delta Calculator Component

## Purpose 
Calculates the perceptual difference (Delta E) between two RGB colors using the colour‑science library.

It enables direct comparison of colors and detection of color shifts, making it useful for tasks such as UI regression testing, brand‑compliance checks, or any workflow that needs to flag noticeable visual changes.

## Technologies
Python, colour‑science

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
from delta_calculator import calculate_delta_e

color1 = [255, 0, 0]  # Red
color2 = [0, 255, 0]  # Green
delta_e = calculate_delta_e(color1, color2)
print(f"Delta E between {color1} and {color2}: {delta_e:.2f}")
```

### Command‑line usage

```bash
python test.py sample_data.csv
```

The script reads the CSV file, computes ΔE for each color pair, and prints the results:

```text
Delta E between [255, 0, 0] and [0, 255, 0]: 170.58
Delta E between [0, 255, 0] and [0, 0, 255]: 258.69
```