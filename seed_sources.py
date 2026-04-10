"""One-time script to seed the knowledge base into Supabase sources table."""
import os
from dotenv import load_dotenv

load_dotenv()

import db


def seed():
    kb_path = os.path.join(os.path.dirname(__file__), "knowledge_base.md")
    if not os.path.exists(kb_path):
        print("knowledge_base.md not found. Copy it into the project root.")
        return

    with open(kb_path, "r", encoding="utf-8") as f:
        content = f.read()

    db.add_source("Татарча диктант — Основная база знаний", content)
    print("Source seeded successfully.")


if __name__ == "__main__":
    seed()
