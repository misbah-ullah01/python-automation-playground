import os
folder_path = "test_files"
files = os.listdir(folder_path)

files.sort()
count = 1

for file_name in files:
    old_path = os.path.join(folder_path, file_name)
    extension = os.path.splitext(file_name)[1]
    new_name = f"vacation_{count:03d}{extension}"
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

    print(f"Renamed: {file_name} -> {new_name}")
    count += 1