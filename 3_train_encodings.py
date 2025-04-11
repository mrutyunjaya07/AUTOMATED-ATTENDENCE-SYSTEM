import face_recognition
import os
import cv2
import pickle

DATASET_DIR = "DATA"
encodings = []
names = []

# Loop through each person's folder
for person_name in os.listdir(DATASET_DIR):
    person_path = os.path.join(DATASET_DIR, person_name)
    if not os.path.isdir(person_path):
        continue

    # Loop through each image of the person
    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)
        image = cv2.imread(image_path)
        if image is None:
            continue

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        for encoding in face_encodings:
            encodings.append(encoding)
            names.append(person_name)

# Save as a dictionary with proper types
data = {"encodings": encodings, "names": names}
with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print(f"[INFO] Saved {len(encodings)} face encodings to encodings.pkl")
