# People Counting with Real-Time Logging

This project is a real-time people counting system using OpenCV for object detection. The system captures live feed from a camera, detects people in the frame, and logs the number of people detected into an Excel file whenever there is a change in the count.

## Features
- Real-time people detection using a webcam.
- Logs the number of people detected in the camera feed into an Excel file.
- Only logs data when there is a change in the number of people detected.
- Timestamps each entry in the log for easy tracking.

## Prerequisites
- Python 3.7+
- A camera or webcam connected to your system.

## Project Setup

### 1. Clone the repository
First, clone the project repository from GitHub:

``bash
git clone https://github.com/Harsha0304/Electrono-Amal.git
cd Electrono-Amal
# On Windows
python -m venv env
env\Scripts\activate

# On Mac/Linux
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
