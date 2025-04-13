import face_recognition
import cv2
import pickle
import pandas as pd
from datetime import datetime
import os

# Load known face encodings
with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

# Initialize video capture
cap = cv2.VideoCapture(1)

# Create attendance file if not exists
attendance_file = "attendance.csv"
if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_csv(attendance_file, index=False)

# Load existing data to avoid duplicates
df = pd.read_csv(attendance_file)

print("Press 'q' to stop...")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = face_distances.argmin() if face_distances.size > 0 else None

        name = "Unknown"

        if best_match_index is not None and matches[best_match_index]:
            name = known_names[best_match_index]

            # Prepare timestamp
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")

            # Prevent duplicate attendance on the same day
            if not ((df["Name"] == name) & (df["Date"] == date_str)).any():
                new_entry = {"Name": name, "Date": date_str, "Time": time_str}
                df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
                df.to_csv(attendance_file, index=False)
                print(f"[ATTENDANCE] {name} marked at {time_str} on {date_str}")

        # Draw rectangle and name
        top, right, bottom, left = [v * 4 for v in face_location]  # Scale back up
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
