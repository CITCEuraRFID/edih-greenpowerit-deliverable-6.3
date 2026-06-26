import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp

def detect_objects(image_path, model_path="efficientdet_lite2.tflite"):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Image at {image_path} not found.")
        return

    # Create detector
    base_options = python.BaseOptions(model_asset_path=model_path)

    options = vision.ObjectDetectorOptions(
        base_options=base_options,
        score_threshold=0.5
    )

    detector = vision.ObjectDetector.create_from_options(options)

    # Convert OpenCV image to MediaPipe image
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

    # Run detection
    detection_result = detector.detect(mp_image)

    # Print detections
    for detection in detection_result.detections:
        category = detection.categories[0]

        bbox = detection.bounding_box
        x = bbox.origin_x
        y = bbox.origin_y
        w = bbox.width
        h = bbox.height

        # Draw rectangle
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Draw label
        label = f"{category.category_name} {category.score:.2f}"

        cv2.putText(
            image,
            label,
            (x, max(y - 10, 0)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    cv2.imshow("Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()