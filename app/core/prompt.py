"""
Scribloom のお題生成モジュール。

このモジュールは、日付に基づいて一貫性のある創作お題を生成します。
お題は「テーマ」「ジャンル」「舞台」の3要素で構成され、毎日変化します。

使用技術:
    - Python の random モジュールによる疑似乱数生成
    - 日付ベースのシード固定による再現性の確保
"""

import random
import datetime

THEMES = ["記憶", "孤独", "再会", "AI", "夢", "秘密"]
GENRES = ["SF", "日常", "恋愛", "ホラー", "ファンタジー"]
SETTINGS = ["宇宙船の中", "近未来の東京", "廃墟となった図書館"]

def generate_daily_prompt():
    """
    今日の日付に基づいて創作お題を生成します。

    Returns:
        dict: 以下のキーを含むお題情報
            - 'theme' (str): テーマ（例: "記憶"）
            - 'genre' (str): ジャンル（例: "SF"）
            - 'setting' (str): 舞台（例: "宇宙船の中"）

    Note:
        同じ日付では同じお題が返されるよう、乱数シードを固定しています。
    """
    seed = int(datetime.date.today().strftime("%Y%m%d"))
    random.seed(seed)
    return {
        "theme": random.choice(THEMES),
        "genre": random.choice(GENRES),
        "setting": random.choice(SETTINGS)
    }
