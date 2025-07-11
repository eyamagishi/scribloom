"""
Scribloom のデータスキーマ定義モジュール。

このモジュールでは、創作お題（Prompt）と投稿データ（Post）を
Pydantic モデルとして定義し、型安全なデータ管理を提供します。

使用技術:
    - Pydantic によるバリデーション付きデータ構造
    - datetime.date による日付管理
"""

from pydantic import BaseModel
from datetime import date
from typing import Dict

class Prompt(BaseModel):
    """
    創作お題を表すデータモデル。

    Attributes:
        theme (str): テーマ（例: "記憶"）
        genre (str): ジャンル（例: "SF"）
        setting (str): 舞台（例: "宇宙船の中"）
    """
    theme: str
    genre: str
    setting: str

class Post(BaseModel):
    """
    投稿データを表すデータモデル。

    Attributes:
        date (date): 投稿日
        prompt (Prompt): 使用されたお題
        content (str): 投稿された文章
        word_count (int): 文字数
    """
    date: date
    prompt: Prompt
    content: str
    word_count: int
