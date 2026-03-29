import os
from groq import Groq
from config import Config
import httpx
import logging

class GroqService:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)

    async def transcribe_audio(self, file_path: str) -> str:
        try:
            with open(file_path, "rb") as file:
                transcription = self.client.audio.transcriptions.create(
                    file=(os.path.basename(file_path), file.read()),
                    model=Config.MODEL_WHISPER,
                    response_format="text",
                )
            return transcription
        except Exception as e:
            logging.error(f"Groq Transcribe Error: {e}")
            raise e

    async def extract_vision(self, image_bytes: bytes) -> str:
        # Llama-3.2 Vision on Groq supports base64
        import base64
        base64_image = base64.b64encode(image_bytes).decode('utf-8')
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Extract all financial items, values, and categories from this receipt. Return a clear list."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                },
                            },
                        ],
                    }
                ],
                model=Config.MODEL_VISION,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logging.error(f"Groq Vision Error: {e}")
            raise e

groq_service = GroqService()
