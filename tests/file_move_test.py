import os
import shutil
import unittest

class TestFileMove(unittest.TestCase):

    def setUp(self):
        self.source_folder = "/mnt/e/vids"
        self.target_folder = "/mnt/e/ffmpeg/media"
        self.keyword = "test"

    def test_file_move(self):
        # Move a file that matches the keyword
        test_file = "test_file.txt"
        source_path = os.path.join(self.source_folder, test_file)
        self.target_path = os.path.join(self.target_folder, test_file)
    
        # Create the test file in the source folder
        with open(source_path, 'w') as f:
            f.write("This is a test")
    
    def move_files_with_keyword(self):
        test_file_1 = "file1.txt"
        test_file_2 = "file2.txt"
        source_path_1 = os.path.join(self.source_folder, test_file_1)
        source_path_2 = os.path.join(self.source_folder, test_file_2)

        # Assert that the files have not been moved
        self.assertFalse(os.path.exists(os.path.join(self.target_folder, test_file_1)))
        self.assertFalse(os.path.exists(os.path.join(self.target_folder, test_file_2)))

        # Clean up the files
        os.remove(source_path_1)
        os.remove(source_path_2)

    def test_no_match(self):
        # Move files with no match for the keyword
        test_file_1 = "file1.txt"
        test_file_2 = "file2.txt"
        source_path_1 = os.path.join(self.source_folder, test_file_1)
        source_path_2 = os.path.join(self.source_folder, test_file_2)

        # Create the test files in the source folder
        with open(source_path_1, 'w') as f1, open(source_path_2, 'w') as f2:
            f1.write("Test file 1")
            f2.write("Test file 2")

        # Call the function to be tested
        self.move_files_with_keyword()

if __name__ == '__main__':
    unittest.main()
