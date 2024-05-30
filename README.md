HAND TRACKING PROJECT

This project demonstrates real-time hand tracking using OpenCV and MediaPipe. It captures video from a webcam, detects hand landmarks, and displays them along with the frame rate (FPS).

Features

- Real-time hand tracking using MediaPipe's Hand module.
- Displays hand landmarks on the video feed.
- Calculates and displays FPS (frames per second).

Requirements

- Python 3.7+
- OpenCV
- MediaPipe

Installation

1. Clone the repository:
   bash:
   
   git clone https://github.com/yourusername/hand-tracking-project.git
   cd hand-tracking-project

2. Create and activate a virtual environment (optional but recommended):
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
   pip install opencv-python mediapipe

USAGE 

1. Run the script:
   python HandTrackingModule.py

''A window will open displaying the video feed from your webcam with detected hand landmarks and FPS.''

''Press q to quit the application.''
