from datetime import datetime, timedelta
import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from config import Config
from database.mongo import db
from services.ai_gateway import groq_service
from services.parser import parser_service

# Create instances
bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Logger
logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🤖 **FinBot v2 Ativado!**\n\nMande áudios, fotos de recibos ou apenas escreva seus gastos.\nStack: Groq + PydanticAI + MongoDB.")

@dp.message(F.voice)
async def handle_voice(message: types.Message):
    # Download voice
    voice = message.voice
    file_info = await bot.get_file(voice.file_id)
    file_name = f"/tmp/{voice.file_unique_id}.ogg"
    await bot.download_file(file_info.file_path, file_name)
    
    msg = await message.answer("⏳ Transcrevendo áudio...")
    
    try:
        text = await groq_service.transcribe_audio(file_name)
        await msg.edit_text(f"📝 *Transcrição:* {text}")
        # Process with AI
        await process_text_finance(message, text)
    except Exception as e:
        await msg.edit_text(f"❌ Erro ao transcrever: {e}")
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    file_data = await bot.download_file(file_info.file_path)
    image_bytes = file_data.read()
    
    msg = await message.answer("🧐 Analisando imagem...")
    
    try:
        extraction = await groq_service.extract_vision(image_bytes)
        await msg.edit_text(f"📄 *Extraído:* {extraction}")
        # Process with AI
        await process_text_finance(message, extraction)
    except Exception as e:
        await msg.edit_text(f"❌ Erro ao analisar imagem: {e}")

@dp.message(F.text)
async def handle_text(message: types.Message):
    await process_text_finance(message, message.text)

async def process_text_finance(message: types.Message, text: str):
    # Filter by User ID if needed
    if Config.ALLOWED_USER_IDS and message.from_user.id not in Config.ALLOWED_USER_IDS:
        return

    # Task 7: Structured Registration Logic
    action = await parser_service.parse_message(text)
    logging.info(f"Action: {action.acao}")
    
    if action.acao == "salvar" and action.data:
        # Save to Mongo
        collection = db.ganhos if action.data.tipo == "entrada" else db.gastos
        data_dict = action.data.dict()
        data_dict['created_at'] = datetime.utcnow()
        await collection.insert_one(data_dict)
        
        emoji = "💰" if action.data.tipo == "entrada" else "💸"
        await message.answer(f"{emoji} **Registrado:** {action.data.item}\nValor: R$ {action.data.valor:.2f}\nCategoria: {action.data.categoria}")

    elif action.acao == "multiplo" and action.multiplo:
        for entry in action.multiplo:
            collection = db.ganhos if entry.tipo == "entrada" else db.gastos
            data_dict = entry.dict()
            data_dict['created_at'] = datetime.utcnow()
            await collection.insert_one(data_dict)
        await message.answer(f"✅ Registrados {len(action.multiplo)} itens com sucesso!")

    elif action.acao == "consultar":
        # Task 8: Finance Reports & Insights
        await send_report(message, action.periodo or "mes")

    elif action.acao == "ignorar":
        pass
    else:
        await message.answer("🤔 Não entendi muito bem. Tente algo como 'Gastei 50 no mercado hoje'.")

async def send_report(message: types.Message, periodo: str):
    await message.answer(f"📊 Relatório de {periodo}...")
    hoje = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    
    if periodo == "semana":
        inicio = hoje - timedelta(days=7)
    elif periodo == "hoje":
        inicio = hoje
    else:
        inicio = hoje.replace(day=1) # mês
    
    # Aggregation
    gastos = await db.gastos.find({"created_at": {"$gte": inicio}}).to_list(length=100)
    ganhos = await db.ganhos.find({"created_at": {"$gte": inicio}}).to_list(length=100)
    
    total_saida = sum(g.get('valor', 0) for g in gastos)
    total_entrada = sum(g.get('valor', 0) for g in ganhos)
    
    report = f"💰 **Entradas:** R$ {total_entrada:.2f}\n"
    report += f"💸 **Saídas:** R$ {total_saida:.2f}\n"
    report += f"⚖️ **Saldo:** R$ {total_entrada - total_saida:.2f}"
    
    await message.answer(report)

async def main():
    await db.connect()
    logging.info("Bot starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())