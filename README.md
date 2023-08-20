# Project Description and Documentation

This project is a Python script that moves files from a source directory to a target directory, based on a specified keyword. The script uses the `os` and `shutil` libraries to perform file operations.

## Usage
1. Enter virtual environment - 
2. `source .venv/bin/activate` on linux/macos
3. `.\venv\Scripts\activate` using powershell
4. Specify the paths for the source folder and target folder in the variables `source_folder` and `target_folder` respectively.
5. Set the keyword to search for in the variable `keyword`. The script will move any files that contain the keyword in their filename, regardless of case (case-insensitive comparison).
6. Run the script.


## Functionality
The script walks through the source folder and its subdirectories, searching for files that contain the specified keyword in their filename. When a matching file is found, it is moved to the target folder using `shutil.move()`. The script also prints a message indicating the file that was moved and the target folder it was moved to.

Note: The script assumes that the source folder and target folder paths are valid and accessible.

Feel free to modify this script according to your specific requirements or incorporate it into your own projects.