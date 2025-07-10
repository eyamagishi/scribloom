# app/services/storage.py

import json
from pathlib import Path
from app.models.schemas import Post

DATA_PATH = Path("data/posts.json")

def load_posts() -> dict:
    if not DATA_PATH.exists() or DATA_PATH.stat().st_size == 0:
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_post(post: Post):
    posts = load_posts()
    posts[str(post.date)] = post.model_dump(mode="json")
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
