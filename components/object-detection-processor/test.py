import sys

from detect_objects import detect_objects


def main() -> None:
    """Command‑line helper for object detection.

    Usage:
        python test.py <path_to_image>

    The script reads the image file at the supplied path, runs the
    ``detect_objects`` function and prints any detection results.
    """
    if len(sys.argv) < 2:
        print("Usage: python test.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    detect_objects(image_path)


if __name__ == "__main__":
    main()
