import numpy as np
import colour

def rgb_to_lab(rgb):
    """Convert RGB color to CIE Lab space."""
    rgb = np.asarray(rgb, dtype=float) / 255.0
    xyz = colour.RGB_to_XYZ(rgb, colour.models.RGB_COLOURSPACE_sRGB)
    lab = colour.XYZ_to_Lab(xyz)
    return lab

def calculate_delta_e(color1, color2):
    """Calculate CIE ΔE between two RGB colors."""
    lab1 = rgb_to_lab(color1)
    lab2 = rgb_to_lab(color2)
    return np.linalg.norm(lab1 - lab2)