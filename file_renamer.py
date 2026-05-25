import os
from pathlib import Path
folder_path = input("Please enter Directory Name: ")
path = Path(folder_path)
if path.is_dir():
    files = os.listdir(folder_path)

    files.sort()
    count = 1

    for file_name in files:
        old_path = os.path.join(folder_path, file_name)
        extension = os.path.splitext(file_name)[1]
        new_name = f"evid_{count:03d}{extension}"
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)

        print(f"Renamed: {file_name} -> {new_name}")
        count += 1
else:
    print("Path error...")