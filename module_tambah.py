# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:15:51 2021

@author: gendutkiy
"""

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

INPUT1, INPUT2 = range(2)

def tambah(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask user for input."""
    #fnm=update.message.first_name
    update.message.reply_text(
        f"Masukkan angka pertama !")
    return INPUT1

def bil1(update: Update, context: CallbackContext) -> int:
    bil1.ank=update.message.text
    update.message.reply_text(
        "Masukkan angka kedua !")
    return INPUT2
    
def bil2(update: Update, context: CallbackContext) -> int:
    ank=update.message.text
    hasil=int(bil1.ank)+int(ank)
    update.message.reply_text(
        f"jadi hasilya adalah {hasil}")
    return ConversationHandler.END

def done(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "see youuu")    
    return ConversationHandler.END