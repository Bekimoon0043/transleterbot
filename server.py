import logging
from telethon import TelegramClient, events
from googletrans import Translator

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the translator
translator = Translator()

# Replace with your own values
API_ID = '21078554'
API_HASH = 'fca31798b27a1010122a0ab57e9fdf63'
BOT_TOKEN = '7700365648:AAG4hTpUMHLT2YgLfpgovWYnCAzF6SldOG0'

# Create the Telegram client
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Hello! Send me text to translate to Amharic. 🇪🇹")

@client.on(events.NewMessage(pattern='/help'))
async def help_command(event):
    await event.respond("Send me a text message and I'll translate it to Amharic. 🇪🇹")

@client.on(events.NewMessage)
async def translate_message(event):
    text = event.message.message  # Get the message text
    try:
        # Translate the text to Amharic
        translated = translator.translate(text, dest='am')
        await event.respond(f"Translated to Amharic: {translated.text} 🇦🇱")
    except Exception as e:
        logger.error(f"Translation error: {e}")
        await event.respond("Sorry, I couldn't translate that. 😞")

# Run the bot
if __name__ == '__main__':
    with client:
        client.run_until_disconnected()
