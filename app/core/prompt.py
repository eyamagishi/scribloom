# app/core/prompt.py
import random
import datetime

THEMES = ["記憶", "孤独", "再会", "AI", "夢", "秘密"]
GENRES = ["SF", "日常", "恋愛", "ホラー", "ファンタジー"]
SETTINGS = ["宇宙船の中", "近未来の東京", "廃墟となった図書館"]

def generate_daily_prompt():
    seed = int(datetime.date.today().strftime("%Y%m%d"))
    random.seed(seed)
    return {
        "theme": random.choice(THEMES),
        "genre": random.choice(GENRES),
        "setting": random.choice(SETTINGS)
    }
