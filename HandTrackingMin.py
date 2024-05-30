# Import necessary libraries
import cv2  # OpenCV for image and video processing
import mediapipe as mp  # MediaPipe for hand tracking
import time  # Time library for FPS calculation

# Initialize the video capture object to read from the default camera (index 0)
cap = cv2.VideoCapture(0)

# Initialize MediaPipe hand solutions
mpHands = mp.solutions.hands  # Access the hands module
hands = mpHands.Hands()  # Create a Hands object for hand tracking
mpDraw = mp.solutions.drawing_utils  # Access drawing utilities for drawing landmarks

# Variables to calculate frames per second (FPS)
pTime = 0  # Previous time
cTime = 0  # Current time

# Start an infinite loop to process video frames
while True:
    # Read a frame from the video capture object
    success, img = cap.read()

    # Convert the BGR image to RGB since MediaPipe processes RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image to detect hands
    results = hands.process(imgRGB)

    # Check if any hand landmarks are detected
    if results.multi_hand_landmarks:
        # Iterate over each detected hand
        for handLms in results.multi_hand_landmarks:
            # Iterate over each landmark in the detected hand
            for id, lm in enumerate(handLms.landmark):
                # img.shape gives the height, width, and channels of the image
                h, w, c = img.shape
                # Calculate the pixel coordinates of the landmark
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)  # Print the landmark id and its coordinates

                # Optionally, draw a circle on the landmark
                # if id == 4:  # Uncomment to draw a circle on a specific landmark (e.g., thumb tip)
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # Draw the hand landmarks on the image
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Calculate FPS
    cTime = time.time()  # Get the current time
    fps = 1 / (cTime - pTime)  # Calculate FPS as the inverse of frame time
    pTime = cTime  # Update the previous time

    # Display FPS on the image
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    # Show the processed image in a window
    cv2.imshow('Image', img)

    # Optional: Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
