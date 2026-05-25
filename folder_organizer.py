import os
import shutil

source_folder = "messy_folder"

files = os.listdir(source_folder)

for files_name in files:
    file_path = os.path.join(source_folder, files_name)
    extension = os.path.splitext(files_name)[1].lower()

    if extension in [".jpg", ".png"]:
        category = "Images"
    elif extension in [".pdf", ".docx"]:
        category = "Documents"
    elif extension in [".mp4", ".mov", ".mkv"]:
        category = "Videos"
    else:
        category = "Others"
    
    category_path = os.path.join(source_folder, category)

    os.makedirs(category_path, exist_ok=True)

    destination = os.path.join(category_path, files_name)

    shutil.move(file_path, destination)

    print(f"Moved {files_name} -> {category}")