"""
Scribloom の投稿データ保存・読み込みモジュール。

このクラスは、投稿データ（Post）を JSON ファイルに保存・読み込みする
永続化処理を提供します。日付をキーとした辞書形式で管理されます。

使用技術:
    - pathlib によるファイルパス操作
    - json モジュールによるシリアライズ
    - Pydantic モデルの JSON 変換
"""

import json
from pathlib import Path
from typing import Dict, Any
from app.models.schemas import Post

class Storage:
    """
    Post データの永続化管理クラス。
    """

    def __init__(self, data_path: Path = Path("data/posts.json")):
        self.data_path = data_path

    def load_posts(self) -> Dict[str, Dict[str, Any]]:
        """
        投稿データを JSON ファイルから読み込みます。

        Returns:
            dict: 日付をキーとした投稿データの辞書。
                  ファイルが存在しない、空、または不正な場合は空の辞書を返します。
        """
        if not self.data_path.exists() or self.data_path.stat().st_size == 0:
            return {}

        try:
            return json.loads(self.data_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}

    def save_post(self, post: Post) -> None:
        """
        新しい投稿データを JSON ファイルに保存します。

        Parameters:
            post (Post): 保存対象の投稿データ。

        Note:
            - 既存の投稿データを読み込んだ上で、日付をキーに追加・上書きします。
            - 保存先ディレクトリが存在しない場合は自動作成されます。
        """
        posts = self.load_posts()
        posts[str(post.date)] = post.model_dump(mode="json")
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        self.data_path.write_text(json.dumps(posts, ensure_ascii=False, indent=2), encoding="utf-8")
