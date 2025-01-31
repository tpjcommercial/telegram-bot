from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Directory to save uploaded files
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Please upload your inspection reports as a file.")

# Function to handle file uploads
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document  # Get the uploaded file
    file_id = file.file_id
    file_name = file.file_name

    # Download the file
    new_file = await context.bot.get_file(file_id)
    save_path = os.path.join(UPLOAD_FOLDER, file_name)
    await new_file.download_to_drive(save_path)

    # Reply to the user
    await update.message.reply_text(f"File '{file_name}' uploaded Nandri Vanakkam!")

# Main function to set up the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
    bot_token = os.getenv"BOT_TOKEN"

    # Set up the application
    application = Application.builder().token(bot_token).build()

    # Command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Message handler for files
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

# Fixing the incorrect `name` check
if __name__ == "__main__":
    main()
