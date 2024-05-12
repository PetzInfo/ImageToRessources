import cv2

def test_cameras():
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            print(f"No camera found at index {index}")
        else:
            print(f"Camera found at index {index}!")
            cap.release()
            break
        index += 1
        cap.release()
        if index > 10:  # Adjust the range as needed
            break

#test_cameras()


def capture_image():
    test_cameras()
    # Attempt to open the first available camera
    camera_index = 0  # Change this if the default isn't correct
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('Press "s" to save the image and "q" to quit', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            cv2.imwrite('./images/captured_image.jpg', frame)
            print("Image saved!")
            break
        elif key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return False

    cap.release()
    cv2.destroyAllWindows()
    return True

#capture_image()