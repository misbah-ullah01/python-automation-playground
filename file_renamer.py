import os
folder_path = "test_files"
files = os.listdir(folder_path)

files.sort()
count = 1

for file_name in files:
    old_path = os.path.join(folder_path, file_name)
    extension = os.path.splitext(file_name)[1]
    