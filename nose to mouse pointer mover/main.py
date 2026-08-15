import cv2
import pyautogui
from cvzone.FaceMeshModule import FaceMeshDetector

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize FaceMesh detector
detector = FaceMeshDetector(maxFaces=1)

# Get screen size
screen_w, screen_h = pyautogui.size()

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect face mesh
    img, faces = detector.findFaceMesh(img)

    if faces:
        face = faces[0]

        # Nose tip landmark (id=1)
        nose_x, nose_y = face[1]

        # Mouth landmarks (upper lip id=13, lower lip id=14)
        upper_lip = face[13]
        lower_lip = face[14]
        mouth_open = abs(upper_lip[1] - lower_lip[1]) > 15  # threshold

        if not mouth_open:  # move only when mouth is closed
            # Map camera coords directly to screen coords (no smoothing)
            screen_x = int((nose_x / img.shape[1]) * screen_w)
            screen_y = int((nose_y / img.shape[0]) * screen_h)

            # Invert horizontal direction
            screen_x = screen_w - screen_x

            # Move instantly (super high sensitivity)
            pyautogui.moveTo(screen_x, screen_y)

            # Draw circle on nose
            cv2.circle(img, (nose_x, nose_y), 5, (0, 255, 0), -1)
        else:
            cv2.putText(img, "Mouth open - mouse paused", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Nose Mouse Control - Super Sensitive", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
