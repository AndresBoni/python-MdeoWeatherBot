from telegram.constants import PARSEMODE_MARKDOWN
from telegram.ext import *
from telegram import *
from functools import wraps

import constants as Keys
import weather

keyboard = [ #Keyboard Options
        [KeyboardButton("¡Quiero saber la temperatura! ☀️")],
        [KeyboardButton("¡Quiero saber el pronóstico! 🌧️")]
    ]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

print("Iniciando Bot...")
#Start chat with Keyboard
def start(update, context):      
    update.message.reply_text('¡Hola! ¿Qué necesitas? 😊', reply_markup=reply_markup)
        
def handle_message(update, context):
    text = str(update.message.text).lower()

    if text == "¡quiero saber la temperatura! ☀️":
        clima(update)
        pass

    elif text == "¡quiero saber el pronóstico! 🌧️":
        forecast(update) #TODO programar esta función
        pass
    
    else:
        no_response(update)
        pass

def clima(update):
    my_weather = weather.get_weather()
    update.message.reply_text(my_weather)

def forecast(update):
    my_forecast = weather.get_forecast()
    update.message.reply_text(my_forecast, PARSEMODE_MARKDOWN)

def no_response(update):
    response = "Lo siento, todavía no sé responder eso.\n"
    update.message.reply_text(response) 
    response = "Puedes consultarme utilizando el menú del teclado."
    update.message.reply_text(response, reply_markup=reply_markup)

def error(update, context):
    print(f"Update {update} error -> {context.error}")

def main():
    updater = Updater(Keys.TELEGRAM_BOT_KEY, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()

