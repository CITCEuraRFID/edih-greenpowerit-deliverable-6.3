from pathlib import Path
import sys
from delta_calculator import calculate_delta_e

if __name__ == "__main__":
    # read CSV with two rows of RGB values separated by comma
    if len(sys.argv) != 2:
        print("Usage: python delta_calculator.py <path_to_sample_csv>")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    lines = [line.strip() for line in csv_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    for line in lines:
        color1_str, color2_str = line.split(",")
        color1 = [int(v) for v in color1_str.split()]
        color2 = [int(v) for v in color2_str.split()]
        delta_e = calculate_delta_e(color1, color2)
        print(f"Delta E between {color1} and {color2}: {delta_e:.2f}")