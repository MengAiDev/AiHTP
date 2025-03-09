from const import const
from kimi.kimi import KimiVisionClient
from fileutils.main import list_files_in_folder

client = KimiVisionClient(const.KIMI_API_KEY)
file_paths = list_files_in_folder(const.EXAMPLE_CALLKIMI_FOLDER_PATH)
messages = client.upload_files(file_paths)

user_question = const.EXAMPLE_CALLKIMI_USER_QUESTION
answer = client.ask_vision_model(messages, user_question)
print("Kimi answer:", answer)