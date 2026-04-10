STRINGS = {
    "ru": {
        "welcome": (
            "👋 Добро пожаловать! Я бот акции «Татарча диктант».\n\n"
            "Задайте мне вопрос о мероприятии, и я постараюсь ответить.\n\n"
            "🌐 Сменить язык: /lang"
        ),
        "help": (
            "ℹ️ Я отвечаю на вопросы об акции «Татарча диктант».\n\n"
            "Просто напишите вопрос в чат.\n\n"
            "Команды:\n"
            "/start — начать\n"
            "/lang — сменить язык\n"
            "/help — помощь"
        ),
        "choose_lang": "🌐 Выберите язык / Тел сайлагыз / Choose language:",
        "lang_set": "✅ Язык установлен: Русский",
        "too_long": "⚠️ Вопрос слишком длинный. Максимум {limit} символов.",
        "thinking": "⏳ Думаю...",
        "off_topic": (
            "⚠️ Я могу отвечать только на вопросы, связанные с акцией «Татарча диктант».\n"
            "Пожалуйста, задайте вопрос по теме мероприятия."
        ),
        "error": "❌ Произошла ошибка. Попробуйте позже.",
        "system_lang": "русском",
    },
    "tt": {
        "welcome": (
            "👋 Рәхим итегез! Мин «Татарча диктант» акциясенең ботымын.\n\n"
            "Чара турында сорау бирегез, мин җавап бирергә тырышырмын.\n\n"
            "🌐 Тел алмаштыру: /lang"
        ),
        "help": (
            "ℹ️ Мин «Татарча диктант» акциясе турында сорауларга җавап бирәм.\n\n"
            "Чатка сорауыгызны языгыз.\n\n"
            "Командалар:\n"
            "/start — башлау\n"
            "/lang — тел алмаштыру\n"
            "/help — ярдәм"
        ),
        "choose_lang": "🌐 Тел сайлагыз / Выберите язык / Choose language:",
        "lang_set": "✅ Тел сайланды: Татарча",
        "too_long": "⚠️ Сорау артык озын. Максимум {limit} символ.",
        "thinking": "⏳ Уйлыйм...",
        "off_topic": (
            "⚠️ Мин «Татарча диктант» акциясе белән генә бәйле сорауларга җавап бирә алам.\n"
            "Зинһар, чара темасы буенча сорау бирегез."
        ),
        "error": "❌ Хата булды. Соңрак тырышып карагыз.",
        "system_lang": "татар",
    },
    "en": {
        "welcome": (
            "👋 Welcome! I'm the «Tatarcha Dictant» event bot.\n\n"
            "Ask me a question about the event and I'll try to answer.\n\n"
            "🌐 Change language: /lang"
        ),
        "help": (
            "ℹ️ I answer questions about the «Tatarcha Dictant» event.\n\n"
            "Just type your question in the chat.\n\n"
            "Commands:\n"
            "/start — start\n"
            "/lang — change language\n"
            "/help — help"
        ),
        "choose_lang": "🌐 Choose language / Тел сайлагыз / Выберите язык:",
        "lang_set": "✅ Language set: English",
        "too_long": "⚠️ Question is too long. Maximum {limit} characters.",
        "thinking": "⏳ Thinking...",
        "off_topic": (
            "⚠️ I can only answer questions related to the «Tatarcha Dictant» event.\n"
            "Please ask a question about the event."
        ),
        "error": "❌ An error occurred. Please try again later.",
        "system_lang": "English",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    text = STRINGS.get(lang, STRINGS["ru"]).get(key, STRINGS["ru"].get(key, key))
    if kwargs:
        text = text.format(**kwargs)
    return text
