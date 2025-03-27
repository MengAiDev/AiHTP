from openai import OpenAI

class DeepSeekV3Client:
    def __init__(self, api_key, model_version="deepseek-v3-0324"):
        self.client = OpenAI(
            base_url="https://api.deepseek.com/v1",
            api_key=api_key
        )
        self.model_version = model_version

    def chat(self, prompt):
        """
        Single-turn conversation with DeepSeek V3
        Args:
            prompt: User input text
            
        Returns:
            str: Model generated response
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.model_version,
                messages=[{"role": "user", "content": prompt}]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"API Error: {str(e)}"
