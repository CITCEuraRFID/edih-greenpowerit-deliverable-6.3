from pyzbar import pyzbar
from PIL import Image
from typing import Optional


def read_qr_code(image_path: str) -> Optional[str]:
    """
    Decode QR code from the given image file.

    Args:
        image_path: Path to image file.

    Returns:
        Decoded QR code data as string, or None if no QR code is found.
    """
    try:
        image = Image.open(image_path)
        decoded = pyzbar.decode(image)
        if decoded:
            return decoded[0].data.decode("utf-8")
        return None
    except Exception:
        return None