from motor.motor_asyncio import AsyncIOMotorClient
from config import Config
import logging

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None
        self.gastos = None
        self.ganhos = None
        self.configs = None

    async def connect(self):
        try:
            self.client = AsyncIOMotorClient(Config.MONGO_URI)
            self.db = self.client[Config.DB_NAME]
            self.gastos = self.db['gastos']
            self.ganhos = self.db['ganhos']
            self.configs = self.db['configuracoes']
            logging.info("MongoDB: Connected successfully!")
        except Exception as e:
            logging.error(f"MongoDB: Connection error: {e}")
            raise e

    async def close(self):
        if self.client:
            self.client.close()

db = MongoDB()
