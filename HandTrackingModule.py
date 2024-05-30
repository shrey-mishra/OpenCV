# Import necessary libraries
import cv2  # OpenCV for image and video processing
import mediapipe as mp  # MediaPipe for hand tracking
import time  # Time library for FPS calculation

class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mpHands = mp.solutions.hands  # Access the hands module
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_con,
            min_tracking_confidence=self.track_con
        )  # Create a Hands object for hand tracking
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process the RGB image to detect hands
        self.results = self.hands.process(imgRGB)
        # Check if any hand landmarks are detected
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                # Draw the hand landmarks on the image
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

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
        return img

    def find_position(self, img, handNo=0, draw=True):
        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList

def main():
    pTime = 0  # Previous time
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.find_hands(img)
        lmList = detector.find_position(img)
        if lmList:
            print(lmList[0])

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

if __name__ == "__main__":
    main()
