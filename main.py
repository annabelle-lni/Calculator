import cv2
import os
import shutil

from save import move_screen
folder_name = "path_label"

# Instructions
print("📰 Instructions: Press 'SPACE' for a screenshot or 'ESC' to exit.")
print("📰 Instructions: There are 4 steps for image processing:")
print("     # screenshot\n     # grayscale\n     # invert colors\n     # contrast")

# Activate the camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Unable to open the camera.")
    exit()

while True:
    # Read the image from the camera
    ret, frame = camera.read()
    if not ret:
        print("Error: Unable to read the video.")
        break

    # Video feed
    cv2.imshow("Camera", frame)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    if key == 32:  # SPACE for the screenshot
        # Screenshot
        cv2.imwrite("screen1.jpg", frame)
        move_screen("screen1.jpg", folder_name)

        # Convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("screen2.jpg", gray_frame)
        move_screen("screen2.jpg", folder_name)

        # Adaptive thresholding
        adaptive_thresh = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        cv2.imwrite("screen3.jpg", adaptive_thresh)
        move_screen("screen3.jpg", folder_name)

        # Median filter
        image_filtered = cv2.medianBlur(adaptive_thresh, 9)
        cv2.imwrite("screen4.jpg", image_filtered)
        move_screen("screen4.jpg", folder_name)

        from addtextfile import addtext  # Add text
        from detection import detection_image #detection

        break

    elif key == 27:  # ESC = exit
        break

camera.release()
cv2.destroyAllWindows()
