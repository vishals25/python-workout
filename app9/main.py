from itertools import count
import cv2, glob
from websocket import send
from emailing import send_mail
import time
import os
from threading import Thread

# Initializing video capture from the default camera
video = cv2.VideoCapture(0)
time.sleep(1)  # Allow the camera to warm up

status_list = []  # To track the status of motion detection
first_frame = None  # To store the first frame for background subtraction
count = 0  # To count and name saved images

def clean_folder():
    # Function to clean the images folder by removing all PNG files
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)

while True:
    status = 0  # Reset status for each frame
    check, frame = video.read()  # Read a frame from the video capture
    if not check:
        break  # Exit if frame is not read successfully

    # Pre-Processing Frames
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)  # Apply Gaussian Blur

    if first_frame is None:
        first_frame = gray_frame_gau  # Set the first frame for background subtraction

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)  # Compute difference between first frame and current frame

    thres_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]  # Apply threshold to get binary image

    dil_frame = cv2.dilate(thres_frame, None, iterations=2) # type: ignore # Dilate the threshold image to fill in holes

    # Optional: Add timestamp to the frame
    # now = datetime.now()
    # cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
    # cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 120), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

    # Display the threshold frame
    cv2.imshow("vid", thres_frame)

    # Find contours in the dilated frame
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue  # Ignore small contours

        x, y, w, h = cv2.boundingRect(contour)  # Get bounding box for the contour
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)  # Draw rectangle around the contour
        if rectangle.any():
            status = 1  # Set status to 1 if motion is detected
            cv2.imwrite(f"images/{count}.png", frame)  # Save the frame with motion detected
            count += 1  # Increment the count for image naming
            all_imgs = glob.glob("images/*.png")
            image = all_imgs[len(all_imgs) // 2]  # Select an image to send via email

    status_list.append(status)
    status_list = status_list[-2:]  # Keep only the last two status

    if status_list[0] == 1 and status_list[1] == 0:
        # Send an email if motion was detected and then stopped
        email_thread = Thread(target=send_mail, args=(image,))
        email_thread.daemon = True
        email_thread.start()

    # Display the frame with contours
    cv2.imshow("vid", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break  # Exit loop if 'q' key is pressed

# Clean the images folder after exiting the loop
clean_thread = Thread(target=clean_folder)
clean_thread.daemon = True
clean_thread.start()

video.release()  # Release the video capture
