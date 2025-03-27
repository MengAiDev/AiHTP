# Cli of Ai HTP
from ai_api import kimi, deepseek
from const import const
from fileutils.main import list_files_in_folder

htp_image_reader = kimi.KimiVisionClient(const.KIMI_API_KEY)
htp_report_completer = deepseek.DeepSeekV3Client(const.DEEPSEEK_API_KEY)

htp_image_path = input("Please input a valid path to htp image")
file_paths = list_files_in_folder("../kimi_knowledge") + [htp_image_path]

print("please wait for kimi's reply...")

messages = htp_image_reader.upload_files(file_paths)
kimi_answer = htp_image_reader.ask_vision_model(messages, "There is a htp test image. And there are also some papers. What can you get?")

print("kimi's reply", kimi_answer)

print("please wait for deepseek's reply...")

deepseek_answer = htp_report_completer.chat(f"You are a expert working on Htp image tests. Here is a result (not detailed): {kimi_answer}. Please complete the report. ")

print("deepseek's reply", deepseek_answer)

print("\nThank you for using Ai HTP!")