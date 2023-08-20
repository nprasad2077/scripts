import unittest
from pathlib import Path
import shutil

class FileMoveTestCase(unittest.TestCase):
    def setUp(self):
        self.source_folder = Path('/path/to/source/')
        self.target_folder = Path('/path/to/target/')
        
        # Create some temporary files for testing
        source_file1 = self.source_folder / 'file1.txt'
        source_file2 = self.source_folder / 'file2.txt'
        source_file3 = self.source_folder / 'file3.txt'
        
        source_file1.write_text('This is file 1')
        source_file2.write_text('This is file 2')
        source_file3.write_text('This is file 3')
        
    def test_file_move(self):
        keyword = 'file'
        expected_files = ['file1.txt', 'file2.txt', 'file3.txt']
        
        # Run code under test
        for file_path in self.source_folder.glob('**/*'):
            if keyword in file_path.name.lower():
                target_path = self.target_folder / file_path.relative_to(self.source_folder)
                target_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.rename(target_path)
                
        # Assert that the files were moved as expected
        actual_files = [file_path.name for file_path in self.target_folder.glob('**/*')]
        self.assertEqual(actual_files, expected_files)
        
    def tearDown(self):
        # Remove the temporary files and folders created during testing
        shutil.rmtree(self.source_folder)
        shutil.rmtree(self.target_folder)

if __name__ == '__main__':
    unittest.main()
