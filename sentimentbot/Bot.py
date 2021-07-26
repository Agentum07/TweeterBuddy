import Constants as keys
from telegram.ext import *
from telegram import Update
import Model as model
import os
PORT = int(os.environ.get('PORT', 5000))

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something and get a sentiment analysis')
    
def help_command(update, context):
    update.message.reply_text('If you need help, you should ask for it on Google!')
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = model.input(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} caused error {context.error}")
    
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    
    dp.add_handler(CommandHandler("help", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    dp.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=keys.API_KEY)
    updater.bot.setWebhook('https://tomatinator.herokuapp.com/' + keys.API_KEY)
    
    updater.idle()

if __name__ == '__main__':
    main()
    
bot.run(keys.API_KEY)
