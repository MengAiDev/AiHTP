from openai import OpenAI
from pathlib import Path

class KimiVisionClient:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.moonshot.cn/v1"
        )

    def upload_files(self, file_paths):
        messages = []
        for file_path in file_paths:
            file_object = self.client.files.create(
                file=Path(file_path),
                purpose="file-extract"
            )
            file_content = self.client.files.content(file_id=file_object.id).text
            messages.append({
                "role": "system",
                "content": file_content
            })
        return messages

    def ask_vision_model(self, messages, user_question):
        messages.append({"role": "user", "content": user_question})
        completion = self.client.chat.completions.create(
            model="moonshot-v1-32k-vision-preview",  # 使用32k模型
            messages=messages,
            temperature=0.3
        )
        return completion.choices[0].message.content