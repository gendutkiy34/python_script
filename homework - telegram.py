# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:44:12 2021

@author: gendutkiy
"""

import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

INPUT1, INPUT2 = range(2)

def tambah(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask user for input."""
    tambah.check="1000"
    update.message.reply_text(
        "Berapa angka pertama yang mau ditambah?")
    return INPUT1

def kurang(update: Update, context: CallbackContext) -> int:
    tambah.check="0100"
    update.message.reply_text(
        "Berapa angka pertama yang mau dikurang")
    return INPUT1

def kali(update: Update, context: CallbackContext) -> int:
    tambah.check="0010"
    update.message.reply_text(
        "Berapa angka pertama yang mau dikali")
    return INPUT1

def bagi(update: Update, context: CallbackContext) -> int:
    tambah.check="0001"
    update.message.reply_text(
        "Berapa angka pertama yang mau dibagi")
    return INPUT1

def bil1(update: Update, context: CallbackContext) -> int:
    bil1.ank=update.message.text
    if tambah.check == "1000":
        pesan="Berapa angka kedua yang mau ditambah?"
    elif tambah.check == "0100":
        pesan="Berapa angka kedua yang mau dikurang?"
    elif tambah.check == "0010":
        pesan="Berapa angka kedua yang mau dikali?"
    elif tambah.check == "0001":
        pesan="Berapa angka kedua yang mau dibagi?"
    update.message.reply_text(pesan)
    return INPUT2
    
def bil2(update: Update, context: CallbackContext) -> int:
    ank=update.message.text
    if tambah.check == "1000":
        opers="penjumlahan"
        hasil=int(bil1.ank)+int(ank)
    elif tambah.check == "0100" :
        opers="pengurangan"
        hasil=int(bil1.ank)-int(ank)
    elif tambah.check == "0010" :
        opers="perkalian"
        hasil=int(bil1.ank)*int(ank)
    elif tambah.check == "0001" :
        opers="pembagian"
        hasil=int(bil1.ank)/int(ank)
     
    update.message.reply_text(
        f"Jadi hasil dari operasi {opers} adalah {hasil}")
    txt=""
    return ConversationHandler.END

def done(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "see youuu")    
    return ConversationHandler.END

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1515311411:AAHeE5G6HfPGt9Wg4y1MNqG8MYvxIxgCbq8")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('tambah', tambah)],
        states={
            INPUT1: [
                MessageHandler(Filters.text, bil1),
            ],
            INPUT2: [
                MessageHandler(Filters.text, bil2),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    conv_handler2 = ConversationHandler(
        entry_points=[CommandHandler('kurang', kurang)],
        states={
            INPUT1: [
                MessageHandler(Filters.text, bil1),
            ],
            INPUT2: [
                MessageHandler(Filters.text, bil2),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    conv_handler3 = ConversationHandler(
        entry_points=[CommandHandler('kali', kali)],
        states={
            INPUT1: [
                MessageHandler(Filters.text, bil1),
            ],
            INPUT2: [
                MessageHandler(Filters.text, bil2),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )
    conv_handler4 = ConversationHandler(
        entry_points=[CommandHandler('bagi', bagi)],
        states={
            INPUT1: [
                MessageHandler(Filters.text, bil1),
            ],
            INPUT2: [
                MessageHandler(Filters.text, bil2),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(conv_handler2)
    dispatcher.add_handler(conv_handler3)
    dispatcher.add_handler(conv_handler4)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()