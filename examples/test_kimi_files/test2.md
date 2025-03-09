Sure! Here is a Python function that lists all the file paths in a folder and returns them as a list.

```python name=list_files_in_folder.py
import os

def list_files_in_folder(folder_path):
    """
    Lists all files' paths in the given folder.

    Args:
    folder_path (str): The path to the folder.

    Returns:
    List[str]: A list of file paths.
    """
    file_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

# Example usage
if __name__ == "__main__":
    folder_path = "path/to/your/folder"
    file_paths = list_files_in_folder(folder_path)
    for path in file_paths:
        print(path)
```

Replace `"path/to/your/folder"` with the actual path to the folder you want to list the files from. This function uses `os.walk` to traverse the directory tree and collect all file paths.