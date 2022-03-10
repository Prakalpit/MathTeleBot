import constants as keys
from telegram.ext import *
import responses as r

print("bot started!!!!")

def start_command(update, context):
    update.message.reply_text("Hey, please type sections to get the sections details")

def handle_message(update,context):

    text = str(update.message.text).lower()
    reply = r.sample_response(text)
    update.message.reply_text(reply)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling(0)
    updater.idle()

main()