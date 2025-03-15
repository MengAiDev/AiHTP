import unittest
import tempfile
import os
from fileutils.main import list_files_in_folder

class TestListFilesInFolder(unittest.TestCase):
    def test_empty_folder(self):
        # 创建一个临时空文件夹
        with tempfile.TemporaryDirectory() as temp_dir:
            # 调用函数
            result = list_files_in_folder(temp_dir)
            # 验证结果
            self.assertEqual(result, [], "空文件夹应返回空列表")

    def test_folder_with_files(self):
        # 创建一个临时文件夹并添加一些文件
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建测试文件
            file1 = os.path.join(temp_dir, "file1.txt")
            file2 = os.path.join(temp_dir, "file2.jpg")
            with open(file1, "w") as f:
                f.write("Test content 1")
            with open(file2, "w") as f:
                f.write("Test content 2")
            
            # 调用函数
            result = list_files_in_folder(temp_dir)
            
            # 验证结果
            expected = [file1, file2]
            self.assertEqual(set(result), set(expected), "应返回所有文件路径")

    def test_folder_with_subfolders(self):
        # 创建一个包含子文件夹和文件的临时文件夹
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建子文件夹和文件
            subfolder = os.path.join(temp_dir, "subfolder")
            os.makedirs(subfolder)
            file1 = os.path.join(temp_dir, "file1.txt")
            file2 = os.path.join(subfolder, "file2.jpg")
            with open(file1, "w") as f:
                f.write("Test content 1")
            with open(file2, "w") as f:
                f.write("Test content 2")
            
            # 调用函数
            result = list_files_in_folder(temp_dir)
            
            # 验证结果
            expected = [file1, file2]
            self.assertEqual(set(result), set(expected), "应返回所有文件路径，包括子文件夹中的文件")

if __name__ == '__main__':
    unittest.main()