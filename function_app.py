import logging
import azure.functions as func
from pyrogram import Client, filters

# Authenticate with Telegram (replace with your actual credentials)
api_id = 21588567
api_hash = "78240039842b973f5139136864b6648f"
bot_token = "6946044714:AAECjchZJkcvXmxcuYzcnI4yPvXtev2eX-o"

# Target chat ID
CHAT_ID = -1002139412083

# Initialize the Telegram bot client
bot = Client("yeshpal_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@func.timer_trigger(schedule="*/30 * * * * *")  # Trigger every 30 seconds
def run_telegram_bot(timer: func.TimerRequest) -> None:
    logging.info('Function triggered')

    try:
        msg = bot.send_message(chat_id=CHAT_ID, text="I am alive!")  # Send the message
        logging.info(f"Message sent: {msg}")  # Log message details
    except Exception as e:
        logging.error(f"Error sending message: {e}")  # Log errors for troubleshooting

    # Remove unnecessary `bot.run()` call, as it's not suitable for Azure Functions
