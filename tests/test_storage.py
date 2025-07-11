"""
storage モジュールの投稿保存・読み込み機能に関するテスト。

このテストでは、Post モデルの保存・読み込み処理が正しく動作すること、
および空ファイルや壊れた JSON に対するフォールバック処理を確認します。

使用技術:
    - pytest によるテスト実行
    - tempfile による一時ファイル生成
    - monkeypatch による DATA_PATH の差し替え
"""

import json
import tempfile
from pathlib import Path
from datetime import date
from app.models.schemas import Prompt, Post
from app.services import storage

def test_save_and_load_post(monkeypatch):
    """
    投稿データを保存し、正しく読み込めることを確認するテスト。

    - 一時ファイルに保存された JSON を読み込み
    - 投稿内容（テーマ・本文）が正しく保持されているか検証
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir) / "posts.json"
        monkeypatch.setattr(storage, "DATA_PATH", test_path)

        prompt = Prompt(theme="記憶", genre="SF", setting="宇宙船の中")
        post = Post(
            date=date(2025, 7, 10),
            prompt=prompt,
            content="彼は記憶を失った状態で目を覚ました。",
            word_count=20
        )

        storage.save_post(post)
        loaded = storage.load_posts()

        assert "2025-07-10" in loaded
        assert loaded["2025-07-10"]["prompt"]["theme"] == "記憶"
        assert loaded["2025-07-10"]["content"].startswith("彼は記憶を")

def test_load_posts_with_empty_file(monkeypatch):
    """
    空の JSON ファイルを読み込んだ場合に空の辞書が返ることを確認するテスト。
    """
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        tmp.write("")  # 空ファイル

    monkeypatch.setattr(storage, "DATA_PATH", tmp_path)
    posts = storage.load_posts()
    assert posts == {}

def test_load_posts_with_invalid_json(monkeypatch):
    """
    壊れた JSON ファイルを読み込んだ場合に空の辞書が返ることを確認するテスト。
    """
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        tmp.write("{ invalid json }")  # 壊れたJSON

    monkeypatch.setattr(storage, "DATA_PATH", tmp_path)
    posts = storage.load_posts()
    assert posts == {}
