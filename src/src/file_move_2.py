import os
import shutil

def move_all_files_and_folders(src_dir, dest_dir):
    # Check if the source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return
    
    # Check if the destination directory exists, create it if not
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate through all files and folders in the source directory
    for item in os.listdir(src_dir):
        src_item_path = os.path.join(src_dir, item)
        dest_item_path = os.path.join(dest_dir, item)

        # Move the item to the destination directory
        shutil.move(src_item_path, dest_item_path)
        print(f"Moved {src_item_path} to {dest_item_path}")

if __name__ == "__main__":
    source_directory = "/e/transfer"
    destination_directory = "/home/ravi/code/scripts"
    move_all_files_and_folders(source_directory, destination_directory)
