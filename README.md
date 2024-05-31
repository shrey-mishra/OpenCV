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
   
   git clone
```python https://github.com/shrey-mishra/hand-tracking-project.git
   cd hand-tracking-project```


2. Create and activate a virtual environment (optional but recommended):
   ````python
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate````

3. Install the required packages:
   pip install opencv-python mediapipe

USAGE 

1. Run the script:
   ```python
python HandTrackingModule.py```

''A window will open displaying the video feed from your webcam with detected hand landmarks and FPS.''

''Press q to quit the application.''


Integration with Major Projects

The HandDetector module is highly versatile and can be seamlessly integrated into various major projects that require hand gesture recognition and tracking. Whether you're working on a virtual reality application, a gesture-based user interface, or a robotics project, this module provides robust hand tracking capabilities. By leveraging MediaPipe's advanced hand tracking technology, the HandDetector can be used to detect and analyze hand movements in real-time, enabling intuitive and interactive experiences. Its ease of use and modular design allow developers to incorporate it into existing projects with minimal modifications, making it an excellent choice for enhancing human-computer interaction in diverse applications.
