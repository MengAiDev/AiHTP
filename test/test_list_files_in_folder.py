import unittest
import tempfile
import os
from fileutils.main import list_files_in_folder

class TestListFilesInFolder(unittest.TestCase):
    def test_empty_folder(self):
        # Create a temporary empty folder
        with tempfile.TemporaryDirectory() as temp_dir:
            # Call the function
            result = list_files_in_folder(temp_dir)
            # Verify the result
            self.assertEqual(result, [], "An empty folder should return an empty list")

    def test_folder_with_files(self):
        # Create a temporary folder and add some files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test files
            file1 = os.path.join(temp_dir, "file1.txt")
            file2 = os.path.join(temp_dir, "file2.jpg")
            with open(file1, "w") as f:
                f.write("Test content 1")
            with open(file2, "w") as f:
                f.write("Test content 2")
            
            # Call the function
            result = list_files_in_folder(temp_dir)
            
            # Verify the result
            expected = [file1, file2]
            self.assertEqual(set(result), set(expected), "Should return all file paths")

    def test_folder_with_subfolders(self):
        # Create a temporary folder with subfolders and files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create subfolder and files
            subfolder = os.path.join(temp_dir, "subfolder")
            os.makedirs(subfolder)
            file1 = os.path.join(temp_dir, "file1.txt")
            file2 = os.path.join(subfolder, "file2.jpg")
            with open(file1, "w") as f:
                f.write("Test content 1")
            with open(file2, "w") as f:
                f.write("Test content 2")
            
            # Call the function
            result = list_files_in_folder(temp_dir)
            
            # Verify the result
            expected = [file1, file2]
            self.assertEqual(set(result), set(expected), "Should return all file paths, including those in subfolders")

if __name__ == '__main__':
    unittest.main()