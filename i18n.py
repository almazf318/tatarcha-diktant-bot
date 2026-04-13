STRINGS = {
    "ru": {
        "welcome": (
            "Исәнмесез! 👋\n\n"
            "Я — бот акции «Татарча диктант».\n"
            "Задайте вопрос о мероприятии — я постараюсь помочь."
        ),
        "help": (
            "ℹ️ Я отвечаю на вопросы об акции «Татарча диктант».\n\n"
            "Просто напишите ваш вопрос в чат — "
            "например, «Когда будет диктант?» или «Как участвовать онлайн?»."
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
        "btn_help": "ℹ️ Ярдәм / Помощь",
        "btn_lang": "🌐 Тел / Язык",
    },
    "tt": {
        "welcome": (
            "Исәнмесез! 👋\n\n"
            "Мин — «Татарча диктант» акциясе буенча ярдәмче бот.\n"
            "Чара хакында нинди дә булса сораулар булса — ярдәм итәргә тырышырмын."
        ),
        "help": (
            "ℹ️ Мин «Татарча диктант» акциясе хакында сорауларга җавап бирәм.\n\n"
            "Сорауыгызны чатка язып җибәрегез — "
            "мәсәлән, «Диктант кайчан була?» яки «Онлайн ничек катнашырга?»."
        ),
        "choose_lang": "🌐 Тел сайлагыз / Выберите язык / Choose language:",
        "lang_set": "✅ Тел сайланды: Татарча",
        "too_long": "⚠️ Сорау артык озын. Максимум {limit} символ.",
        "thinking": "⏳ Көтегез...",
        "off_topic": (
            "⚠️ Мин «Татарча диктант» акциясе хакында гына сорауларга җавап бирә алам.\n"
            "Зинһар, чара темасы буенча сорау бирегез."
        ),
        "error": "❌ Хата булды. Соңрак кабат тырышып карагыз.",
        "system_lang": "татар",
        "btn_help": "ℹ️ Ярдәм / Помощь",
        "btn_lang": "🌐 Тел / Язык",
    },
    "en": {
        "welcome": (
            "Isänmesez! 👋\n\n"
            "I'm the «Tatarcha Dictant» assistant bot.\n"
            "Ask me anything about the event — I'll do my best to help."
        ),
        "help": (
            "ℹ️ I answer questions about the «Tatarcha Dictant» event.\n\n"
            "Just type your question — "
            "for example, «When is the dictant?» or «How to participate online?»."
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
        "btn_help": "ℹ️ Ярдәм / Help",
        "btn_lang": "🌐 Тел / Language",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    text = STRINGS.get(lang, STRINGS["ru"]).get(key, STRINGS["ru"].get(key, key))
    if kwargs:
        text = text.format(**kwargs)
    return text
