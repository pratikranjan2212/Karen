import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import youtube_dl

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the message handler
def download_music(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    
    # Check if the message contains a valid link
    if "https://www.youtube.com/watch?v=" in text:
        # Define the options for youtube-dl
        audio_ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'music.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        
        with youtube_dl.YoutubeDL(audio_ydl_opts) as ydl:
            ydl.download([text])

        video_ydl_opts = {
            'format': 'bestvideo[ext=mp4]',
            'outtmpl': 'video.%(ext)s',
        }
        with youtube_dl.YoutubeDL(video_ydl_opts) as ydl:
            ydl.download([text]),
        
        # Send the downloaded file to the user
        context.bot.send_audio(chat_id=chat_id, audio=open('music.mp3', 'rb'), title='Music', performer='Artist')
        context.bot.send_video(chat_id=chat_id, video=open('video.mp4', 'rb'), supports_streaming=True)
    else:
        context.bot.send_message(chat_id=chat_id, text="Invalid link.")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a Telegram bot!")

def main():
    # Create the Updater and pass the bot token
    updater = Updater("6097119860:AAH2x4jgUrgh2Tvv_-ky6nz6Ej0LIJ3P0GQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Define the message handler
    dp.add_handler(MessageHandler(filters.text & ~filters.command, download_music))

    # Start the bot
    start_handler = CommandHandler('start', start)
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
