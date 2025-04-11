import cv2
import os

# Constants
CAPTURE_COUNT = 3
DATASET_DIR = "DATA"

# Create dataset directory if it doesn't exist
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# Get user name input
user_name = input("Enter your name: ").strip().upper()
user_path = os.path.join(DATASET_DIR, user_name)

# Create a folder for this user
if not os.path.exists(user_path):
    os.makedirs(user_path)

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)
count = 0

print("\nCamera started. Press 's' to save image, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the webcam feed
    cv2.imshow("Face Capture - Press 's' to save, 'q' to quit", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and len(faces) > 0:
        # Save the first detected face
        (x, y, w, h) = faces[0]
        face_img = frame[y:y+h, x:x+w]
        img_path = os.path.join(user_path, f"{count + 1}.jpg")
        cv2.imwrite(img_path, face_img)
        count += 1
        print(f"Saved image {count}/{CAPTURE_COUNT}")

        if count >= CAPTURE_COUNT:
            print("Image capture complete.")
            break

    elif key == ord('q'):
        print("Camera closed by user.")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print(f"Total images saved: {count} in '{user_path}'")
