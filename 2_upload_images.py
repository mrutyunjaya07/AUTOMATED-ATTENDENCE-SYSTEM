import os
import shutil
from tkinter import Tk, filedialog

# Constants
DATASET_DIR = "DATA"

# Create dataset directory if it doesn't exist
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# Get user name input
user_name = input("Enter the name for training (person's name): ").strip().upper()
user_path = os.path.join(DATASET_DIR, user_name)

# Create a folder for this user
if not os.path.exists(user_path):
    os.makedirs(user_path)

# Use tkinter to open file dialog for image selection
print("Please select image(s) to upload...")

# Hide the root Tkinter window
Tk().withdraw()

# Allow selecting multiple files
file_paths = filedialog.askopenfilenames(
    title="Select Image(s)",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if not file_paths:
    print("No files selected. Exiting.")
    exit()

# Copy images to user's folder
for idx, file_path in enumerate(file_paths, start=1):
    ext = os.path.splitext(file_path)[1]
    dest_path = os.path.join(user_path, f"{idx}{ext}")
    shutil.copy(file_path, dest_path)

print(f"{len(file_paths)} image(s) uploaded successfully to {user_path}")
