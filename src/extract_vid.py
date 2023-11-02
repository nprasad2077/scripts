import os
import shutil
from colorama import init, Fore, Style

init()
print(Fore.GREEN + "Change to green text for move.")


def move_videos(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith((".mp4", ".mov", ".mkv", ".ts", ".m4v", ".gba")):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                # The shutil.copy2 preserves both the file contents and metadata (such as timestamps) during the copy.
                # shutil.copy2(source_path, dest_path)
                shutil.move(source_path, dest_path)
                print(f"Moved {file} to {dest_dir}")


# Example usage
source_directory = "/e/qb_dl_3"
destination_directory = "/e/qb_dl_3"

# # Uncomment to enable directory input
# source_directory_input = input("Enter src directory: ")
# destination_directory_input = input("Enter the dest directory: ")
# format_source_input = str(source_directory_input)
# format_dest_input = str(destination_directory_input)
# move_videos(format_source_input, format_dest_input)

move_videos(source_directory, destination_directory)

print(Fore.MAGENTA + "COMPLETE.")
