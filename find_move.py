import os
import shutil

# Specify the paths
source_folder = '/mnt/e/property/'
target_folder = '/mnt/d/property_out/'

# Keyword to search for
keyword = input('partial file name: ') # Change the keyword to lowercase for case-insensitive comparison

formatted_string = f"{keyword}"
print(formatted_string)

# Walk through the source folder and its subdirectories
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if keyword.lower() in file.lower(): # Perform case-insensitive comparison
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_folder, file)
            shutil.move(source_path, target_path)
            print(f"Moved {file} to {target_folder}")
        