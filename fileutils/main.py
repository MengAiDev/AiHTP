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
