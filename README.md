# Real-Time Face Detection using OpenCV
This project demonstrates real-time face detection using a webcam and OpenCV's Haar Cascade Classifier.

# 🔍 Overview
Using OpenCV and a pre-trained Haar cascade classifier, the program captures video from your system's webcam and detects human faces in real-time. Detected faces are highlighted with a green rectangle.

# 📂 Project Structure
haarcascade_frontalface_default.xml: Pre-trained Haar cascade file used for face detection (comes with OpenCV).

face_detection.py: Main Python script for capturing webcam video and detecting faces.

# 🚀 How It Works
1. Loads the Haar cascade XML file for detecting frontal faces.
2. Captures video from the system's webcam.
3. Converts each video frame to grayscale for faster processing.
4. Detects faces and draws green rectangles around them.
5. Press S to stop the webcam and exit the program.

📦 Requirements
1. Python 3.x
2. OpenCV
3. Install OpenCV using pip:
      pip install opencv-python

# ▶️ How to Run
1. Clone the repository or download the script.
2. Make sure your webcam is connected and working.
3. Run the script:
     python face_detection.py
4. A window will open showing the video feed with detected faces.
5.Press S key to exit the video.

 # 🧠 Note
The path to the Haar cascade XML file must be correct. It is usually located in:
  <your-python-path>/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml

# 📸 Output
 🙌 Real-time webcam feed with green rectangles drawn around detected faces.


