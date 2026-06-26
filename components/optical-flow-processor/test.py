#!/usr/bin/env python
"""Demo script for OpticalFlowProcessor.

Usage:
    python test.py <image_a> <image_b>
"""

import argparse
import sys
import cv2
import numpy as np
from optical_flow_processor import OpticalFlowProcessor


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Demo for OpticalFlowProcessor: compute dense optical flow between two images."
    )
    parser.add_argument("image_a", help="Path to the first image (grayscale or color).")
    parser.add_argument("image_b", help="Path to the second image (grayscale or color).")
    args = parser.parse_args()

    # Read images – enforce grayscale for the processor
    img1 = cv2.imread(args.image_a, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(args.image_b, cv2.IMREAD_GRAYSCALE)

    if img1 is None:
        sys.exit(f"Error: could not read image {args.image_a}")
    if img2 is None:
        sys.exit(f"Error: could not read image {args.image_b}")

    processor = OpticalFlowProcessor()
    flow = processor.compute_flow(img1, img2)

    print(f"Flow shape: {flow.shape}")

    # Visualise flow magnitude (optional)
    mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    # Scale to 0‑255 and convert to uint8 for PNG output
    mag_norm = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    cv2.imwrite("flow.png", mag_norm)
    print("Flow visualisation saved as flow.png")


if __name__ == "__main__":
    main()
