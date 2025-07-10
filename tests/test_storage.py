# tests/test_storage.py

import json
import tempfile
from pathlib import Path
from datetime import date
from app.models.schemas import Prompt, Post
from app.services import storage

def test_save_and_load_post(monkeypatch):
    # 一時ファイルを作成
    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir) / "posts.json"

        # storage.py の DATA_PATH を一時ファイルに差し替え
        monkeypatch.setattr(storage, "DATA_PATH", test_path)

        # テスト用の投稿データ
        prompt = Prompt(theme="記憶", genre="SF", setting="宇宙船の中")
        post = Post(
            date=date(2025, 7, 10),
            prompt=prompt,
            content="彼は記憶を失った状態で目を覚ました。",
            word_count=20
        )

        # 保存 → 読み込み
        storage.save_post(post)
        loaded = storage.load_posts()

        # 検証
        assert "2025-07-10" in loaded
        assert loaded["2025-07-10"]["prompt"]["theme"] == "記憶"
        assert loaded["2025-07-10"]["content"].startswith("彼は記憶を")
