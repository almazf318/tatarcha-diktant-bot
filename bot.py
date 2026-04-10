import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)
import db
import ai
from i18n import t

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

MAX_QUESTION_LENGTH = int(os.getenv("MAX_QUESTION_LENGTH", "500"))

LANG_MAP = {"lang_ru": "ru", "lang_tt": "tt", "lang_en": "en"}
LANG_SYSTEM = {"ru": "русском", "tt": "татар", "en": "English"}

BTN_HELP_TEXTS = {"ℹ️ Ярдәм / Помощь", "ℹ️ Ярдәм / Help"}
BTN_LANG_TEXTS = {"🌐 Тел / Язык", "🌐 Тел / Language"}


def main_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [[t(lang, "btn_help"), t(lang, "btn_lang")]],
        resize_keyboard=True,
    )


def lang_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Татарча", callback_data="lang_tt"),
                InlineKeyboardButton("Русский", callback_data="lang_ru"),
                InlineKeyboardButton("English", callback_data="lang_en"),
            ]
        ]
    )


async def get_lang(tg_id: int) -> str:
    return db.get_user_lang(tg_id) or "tt"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = await get_lang(user.id)
    db.upsert_user(user.id, user.username, user.first_name, lang)
    await update.message.reply_text(
        t(lang, "welcome"),
        reply_markup=main_keyboard(lang),
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_lang(update.effective_user.id)
    await update.message.reply_text(t(lang, "help"))


async def lang_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_lang(update.effective_user.id)
    await update.message.reply_text(
        t(lang, "choose_lang"),
        reply_markup=lang_inline_keyboard(),
    )


async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang_code = LANG_MAP.get(query.data)
    if not lang_code:
        return
    tg_id = query.from_user.id
    db.set_user_lang(tg_id, lang_code)
    db.upsert_user(tg_id, query.from_user.username, query.from_user.first_name, lang_code)
    await query.edit_message_text(t(lang_code, "lang_set"))
    await query.message.reply_text(
        t(lang_code, "welcome"),
        reply_markup=main_keyboard(lang_code),
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = await get_lang(user.id)
    text = update.message.text.strip()

    # Handle button presses
    if text in BTN_HELP_TEXTS:
        await update.message.reply_text(t(lang, "help"))
        return
    if text in BTN_LANG_TEXTS:
        await update.message.reply_text(
            t(lang, "choose_lang"),
            reply_markup=lang_inline_keyboard(),
        )
        return

    # Question handling
    if len(text) > MAX_QUESTION_LENGTH:
        await update.message.reply_text(t(lang, "too_long", limit=MAX_QUESTION_LENGTH))
        return

    thinking_msg = await update.message.reply_text(t(lang, "thinking"))

    try:
        answer, is_off_topic = ai.ask(text, LANG_SYSTEM.get(lang, "русском"))

        if is_off_topic:
            final_text = t(lang, "off_topic")
        else:
            final_text = answer

        db.log_qa(user.id, text, final_text, lang, is_off_topic)
        await thinking_msg.edit_text(final_text)

    except Exception:
        logger.exception("Error answering question")
        await thinking_msg.edit_text(t(lang, "error"))


def main():
    app = Application.builder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("lang", lang_cmd))
    app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot started")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
