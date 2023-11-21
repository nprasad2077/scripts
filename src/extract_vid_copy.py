import os
import shutil
from colorama import init, Fore, Style

init()
print(Fore.BLUE + "Change to blue text for copy.")

def move_videos(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith((".mp4", ".mov", ".mkv", ".ts")):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                # The shutil.copy2 preserves both the file contents and metadata (such as timestamps) during the copy.
                shutil.copy2(source_path, dest_path)
                # shutil.move(source_path, dest_path)
                print(f"Copied {file} to {dest_dir}")

# Example usage
source_directory = "/j/test"
destination_directory = "/j/test"
move_videos(source_directory, destination_directory)

print(Fore.MAGENTA + 'COMPLETE.')
