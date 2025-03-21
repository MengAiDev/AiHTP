# Cli of Ai HTP
from ai_api import kimi, deepseek
from const import const
from fileutils.main import list_files_in_folder

htp_image_path = input("Please input a valid path to htp image")
file_paths = list_files_in_folder("../kimi_knowledge") + [htp_image_path]

htp_image_reader = kimi.KimiVisionClient(const.KIMI_API_KEY)

