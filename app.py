import cv2
import numpy as np
import pandas as pd
from datetime import datetime

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open webcam (or change to video feed from a file)
cap = cv2.VideoCapture(0)  # Change to '1' or other number for external camera

# Set up Excel logging
excel_file = "people_count_log.xlsx"

# Initialize logging file with headers
def initialize_excel():
    df = pd.DataFrame(columns=["Timestamp", "People_Count"])
    df.to_excel(excel_file, index=False)

# Log the current people count with a timestamp
def log_people_count(count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_new = pd.DataFrame([[timestamp, count]], columns=["Timestamp", "People_Count"])
    
    try:
        # Try to read the existing Excel file
        df_existing = pd.read_excel(excel_file)
        # Append the new data
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    except FileNotFoundError:
        # If the file does not exist, use the new data
        df_combined = df_new
    
    # Save the combined data back to the Excel file
    df_combined.to_excel(excel_file, index=False)

    print(f"Logged: {timestamp} - People Count: {count}")

# Initialize the Excel file
initialize_excel()

# Initialize previous count to -1 (impossible count value)
previous_count = -1

# Process video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame for faster processing
    frame = cv2.resize(frame, (640, 480))

    # Detect people in the frame
    (rects, weights) = hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)

    # Draw bounding boxes around detected people
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Get the current people count
    current_count = len(rects)
    
    # Log the data only if the count has changed
    if current_count != previous_count:
        log_people_count(current_count)
        previous_count = current_count

    # Display the number of people detected
    cv2.putText(frame, f"People Count: {current_count}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow("People Counter", frame)

    # Break loop with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
