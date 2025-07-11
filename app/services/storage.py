"""
Scribloom の投稿データ保存・読み込みモジュール。

このモジュールは、投稿データ（Post）を JSON ファイルに保存・読み込みする
永続化処理を提供します。日付をキーとした辞書形式で管理されます。

使用技術:
    - pathlib によるファイルパス操作
    - json モジュールによるシリアライズ
    - Pydantic モデルの JSON 変換
"""

import json
from pathlib import Path
from app.models.schemas import Post

DATA_PATH = Path("data/posts.json")

def load_posts() -> dict:
    """
    投稿データを JSON ファイルから読み込みます。

    Returns:
        dict: 日付をキーとした投稿データの辞書。
              ファイルが存在しない、空、または不正な場合は空の辞書を返します。
    """
    if not DATA_PATH.exists() or DATA_PATH.stat().st_size == 0:
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_post(post: Post):
    """
    新しい投稿データを JSON ファイルに保存します。

    Parameters:
        post (Post): 保存対象の投稿データ。

    Note:
        - 既存の投稿データを読み込んだ上で、日付をキーに追加・上書きします。
        - 保存先ディレクトリが存在しない場合は自動作成されます。
    """
    posts = load_posts()
    posts[str(post.date)] = post.model_dump(mode="json")
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
