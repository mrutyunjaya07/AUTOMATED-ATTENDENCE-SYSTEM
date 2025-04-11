🧠 Face Detection Attendance System :


📖 Introduction

This project is a Face Detection Attendance System built using Python and Machine Learning. It utilizes a webcam to capture live video, detects faces using OpenCV and face_recognition, and automatically logs the attendance of recognized individuals into a CSV and Excel file with timestamps.


🎯 Objective

The main goal of this project is to replace manual attendance systems with an efficient, real-time, and automatic face recognition-based attendance logger. This ensures accuracy, reduces time, and prevents proxy attendance.


🧰 Technologies Used

- Python : Core programming language

- OpenCV (cv2) : For webcam access and real-time image processing

- face_recognition : For accurate face detection and recognition

- NumPy : For numerical operations

- Pandas : For managing attendance data

- openpyxl : For saving Excel files

- pickle : To save encoded facial data


📁 Project Folder Structure

Face-Attendance-System :

- 1_capture_immages.py          # For capturing images via webcam 
- 2_upload_images.py            # For uploading custom images
- 3_train_encodings.py          # For generating face encodings
- 4_mark_attendance.py             # For real-time attendance using webcam
- requirements.txt              # All required Python packages
- README.md                     # Project documentation

- dataset/                      # Folder with known face images
     - MJ.jpg, Alice.jpg         # Images named after people

- attendance/                   # Folder to store output files
     - Attendance.csv

- encoded_faces.pickle          # Pickle file containing face encodings


🧪 How to Set Up and Run :


1. 🔧 Install Required Libraries :

    Make sure Python is installed. Then run:
     >>> pip install -r requirements.txt

2. 📷 Add Known Faces :

     - Place images of known individuals in the dataset/ folder.
     - File names should match the person’s name. Example: MJ.jpg

3. 🧬 Encode the Faces :

     - Run the following command to generate encodings of known faces:
         >>> python encode_faces.py
     - This creates a file encoded_faces.pickle which stores facial data.

4. 🟢 Start Attendance System :

     - Run the main attendance script
       >>> python attandance_with_photo.py
     - This will open your webcam, detect faces, and mark attendance in:
     
       - attendance/Attendance.csv
     
     - To stop the system, press Q on your keyboard.
     
     
📌 Notes

   - Ensure your webcam is connected and accessible.
     
   - Re-run encode_faces.py every time you add new images to the dataset.
     
   - The face recognition is based on comparing facial encodings, so   
     good-quality images work best.
     

👨‍💻 Developer Info
     