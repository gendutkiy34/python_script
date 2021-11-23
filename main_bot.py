# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:17:11 2021

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
import module_tambah as mt

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

INPUT1, INPUT2 = range(2)


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1515311411:AAHeE5G6HfPGt9Wg4y1MNqG8MYvxIxgCbq8")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('tambah', mt.tambah)],
        states={
            INPUT1: [
                MessageHandler(Filters.text, mt.bil1),
            ],
            INPUT2: [
                MessageHandler(Filters.text, mt.bil2),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), mt.done)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()