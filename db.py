import os
from supabase import create_client, Client

_client: Client | None = None


def get_client() -> Client:
    global _client
    if _client is None:
        _client = create_client(
            os.environ["SUPABASE_URL"],
            os.environ["SUPABASE_KEY"],
        )
    return _client


def upsert_user(tg_id: int, username: str | None, first_name: str | None, lang: str):
    get_client().table("users").upsert(
        {
            "tg_id": tg_id,
            "username": username or "",
            "first_name": first_name or "",
            "lang": lang,
        },
        on_conflict="tg_id",
    ).execute()


def set_user_lang(tg_id: int, lang: str):
    get_client().table("users").update({"lang": lang}).eq("tg_id", tg_id).execute()


def get_user_lang(tg_id: int) -> str | None:
    resp = get_client().table("users").select("lang").eq("tg_id", tg_id).execute()
    if resp.data:
        return resp.data[0]["lang"]
    return None


def log_qa(tg_id: int, question: str, answer: str, lang: str, is_off_topic: bool):
    get_client().table("qa_log").insert(
        {
            "tg_id": tg_id,
            "question": question,
            "answer": answer,
            "lang": lang,
            "is_off_topic": is_off_topic,
        }
    ).execute()


def get_sources() -> list[dict]:
    resp = get_client().table("sources").select("*").eq("active", True).execute()
    return resp.data or []


def add_source(title: str, content: str):
    get_client().table("sources").insert(
        {"title": title, "content": content, "active": True}
    ).execute()
