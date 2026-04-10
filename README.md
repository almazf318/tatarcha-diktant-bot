# Татарча диктант — Telegram Bot

Telegram-бот для ответов на вопросы об акции «Татарча диктант». Работает на трёх языках: татарский, русский, английский.

## Stack

- Python 3.11
- python-telegram-bot
- Google Gemini 2.0 Flash
- Supabase (PostgreSQL)
- Railway (deploy)

## Setup

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in the values
3. Run Supabase migrations (see `schema.sql`)
4. Seed the knowledge base: `python seed_sources.py`
5. Run the bot: `python bot.py`

## Environment Variables

| Variable | Description |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Telegram Bot API token |
| `GEMINI_API_KEY` | Google Gemini API key |
| `SUPABASE_URL` | Supabase project URL |
| `SUPABASE_KEY` | Supabase anon key |
| `MAX_QUESTION_LENGTH` | Max chars per question (default: 500) |

## Commands

- `/start` — Start the bot
- `/lang` — Change language (Татарча / Русский / English)
- `/help` — Help

## Architecture

- `bot.py` — Telegram bot handlers
- `ai.py` — Gemini API integration with topic filtering
- `db.py` — Supabase database operations
- `i18n.py` — Translations for 3 languages
- `seed_sources.py` — Script to load knowledge base into Supabase
- `knowledge_base.md` — Event information
- `schema.sql` — Database schema
