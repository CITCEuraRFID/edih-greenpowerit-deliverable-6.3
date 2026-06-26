"""
Optical Flow Processor
Core implementation for computing dense optical flow between consecutive images.
"""

import cv2
import numpy as np


class OpticalFlowProcessor:
    """
    Compute dense optical flow using Farneback algorithm.

    Parameters
    ----------
    pyr_scale : float, optional
        Image pyramid scale; default 0.5.
    level : int, optional
        Number of pyramid levels; default 3.
    winsize : int, optional
        Size of the pixel neighborhood; default 15.
    iterations : int, optional
        Number of iterations; default 3.
    poly_n : int, optional
        Size of the pixel neighborhood for polynomial expansion; default 5.
    poly_sigma : float, optional
        Standard deviation of Gaussian; default 1.2.
    flags : int, optional
        Optional flags; default 0.
    """

    def __init__(
        self,
        pyr_scale=0.5,
        level=3,
        winsize=15,
        iterations=3,
        poly_n=5,
        poly_sigma=1.2,
        flags=0,
    ):
        self.pyr_scale = pyr_scale
        self.level = level
        self.winsize = winsize
        self.iterations = iterations
        self.poly_n = poly_n
        self.poly_sigma = poly_sigma
        self.flags = flags

    def compute_flow(self, prev_image: np.ndarray, next_image: np.ndarray) -> np.ndarray:
        """
        Calculate optical flow between two consecutive images.

        Parameters
        ----------
        prev_image : np.ndarray
            Previous grayscale image as a 2‑D NumPy array.
        next_image : np.ndarray
            Current grayscale image as a 2‑D NumPy array.

        Returns
        -------
        np.ndarray
            Flow field with shape (H, W, 2) where each (dx, dy) represents
            motion vectors.
        """
        if prev_image.shape != next_image.shape:
            raise ValueError("Input images must have the same dimensions.")
        if prev_image.ndim != 2 or next_image.ndim != 2:
            raise ValueError("Input images must be grayscale (2‑D arrays).")

        flow = cv2.calcOpticalFlowFarneback(
            prev_image,
            next_image,
            None,
            self.pyr_scale,
            self.level,
            self.winsize,
            self.iterations,
            self.poly_n,
            self.poly_sigma,
            self.flags,
        )
        return flow