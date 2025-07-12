"""
Scribloom のお題生成モジュール。

このモジュールは、日付に基づいて一貫性のある創作お題を生成します。
お題は「テーマ」「ジャンル」「舞台」の3要素で構成され、毎日変化します。

使用技術:
    - Python の random モジュールによる疑似乱数生成
    - 日付ベースのシード固定による再現性の確保
    - Prompt モデルによる型安全な構造
"""

import random
import datetime
from app.models.schemas import Prompt

THEMES = ["記憶", "孤独", "再会", "AI", "夢", "秘密"]
GENRES = ["SF", "日常", "恋愛", "ホラー", "ファンタジー"]
SETTINGS = ["宇宙船の中", "近未来の東京", "廃墟となった図書館"]

def generate_daily_prompt() -> Prompt:
    """
    今日の日付に基づいて創作お題を生成します。

    Returns:
        Prompt: テーマ・ジャンル・舞台の3要素からなるお題モデル。

    Note:
        同じ日付では同じお題が返されるよう、乱数シードを固定しています。
    """
    seed = int(datetime.date.today().strftime("%Y%m%d"))
    random.seed(seed)
    return Prompt(
        theme=random.choice(THEMES),
        genre=random.choice(GENRES),
        setting=random.choice(SETTINGS)
    )
