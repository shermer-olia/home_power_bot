import logging

from datetime import datetime

import sys

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.error import NetworkError

TOKEN = sys.argv[1]


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger = logging.getLogger('error_handler')
    if isinstance(context.error, NetworkError):
        pass
    else:
        logger.error(msg=f'Update caused error:', exc_info=context.error)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def check_power(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=u'\U0001f4a1' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    check_power_handler = CommandHandler('check_power', check_power)
    application.add_handler(check_power_handler)

    application.add_error_handler(error_handler)

    application.run_polling()
