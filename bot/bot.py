from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from telegram.ext import filters
from dotenv import load_dotenv
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Benvenuto!")
    #fare protection proxy che controlla l'accesso
    
async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_file = await update.message.effective_attachment.get_file()
    file_name = new_file.file_path
    print("file name ", file_name)
    await new_file.download_to_drive('audio.m4a')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Audio arrivato al server")

if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv("BOT_TOKEN")
    
    application = ApplicationBuilder().token(telegram_token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    

    msg_handler = MessageHandler(filters=filters.ATTACHMENT, callback=callback)
    application.add_handler(msg_handler)
    
    application.run_polling()