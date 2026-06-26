import sys
from qr_code_reader import read_qr_code


def main() -> None:
    """Entry point for the command‑line helper.

    Expected usage:
        python test.py <path_to_image>

    The script reads the image file, runs ``read_qr_code`` on it, and prints the
    decoded QR code data (or ``None`` if no QR code is found).
    """
    if len(sys.argv) < 2:
        print("Usage: python test.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    data = read_qr_code(image_path)
    print(data)


if __name__ == "__main__":
    main()