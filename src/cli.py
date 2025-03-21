# Cli of Ai HTP
from ai_api import kimi, deepseek
from const import const
from fileutils.main import list_files_in_folder

htp_image_path = input("Please input a valid path to htp image")
file_paths = list_files_in_folder("../kimi_knowledge") + [htp_image_path]

htp_image_reader = kimi.KimiVisionClient(const.KIMI_API_KEY)

print("please wait for kimi's reply...")

messages = htp_image_reader.upload_files(file_paths)
kimi_answer = htp_image_reader.ask_vision_model(messages, "There is a htp test image. And there are also some papers. What can you get?")

print("kimi's reply", kimi_answer)

