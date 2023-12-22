import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from music import return_key_and_progression
from secrets import get_bot_token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a MusicTrainer bot. Click /next to get a new key and progression."
    )


async def next_key_progression(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = return_key_and_progression()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=text)


if __name__ == '__main__':
    token = get_bot_token()
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    next_handler = CommandHandler('next', next_key_progression)
    application.add_handler(next_handler)

    application.run_polling()