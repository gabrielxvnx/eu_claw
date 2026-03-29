import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bot Settings
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    ALLOWED_USER_IDS = [int(uid.strip()) for uid in os.getenv("ALLOWED_USER_IDS", "").split(",") if uid.strip()]
    
    # Storage
    # Em Docker, o MONGO_URI deve ser mongodb://mongodb:27017/finbot_db
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/finbot_db")
    DB_NAME = "finbot_db"
    
    # AI Providers
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    MOONSHOT_API_KEY = os.getenv("MOONSHOT_API_KEY")
    
    # Models
    MODEL_EXTRACT = "llama-3.1-70b-versatile" # O Groq as vezes muda os nomes
    MODEL_VISION = "llama-3.2-11b-vision-preview"
    MODEL_WHISPER = "whisper-large-v3"
    MODEL_FALLBACK = "google/gemini-2.0-flash-001" # Exemplo OpenRouter
    
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
