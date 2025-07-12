"""
storage モジュールの投稿保存・読み込み機能に関するテスト。

このテストでは、Post モデルの保存・読み込み処理が正しく動作すること、
および空ファイルや壊れた JSON に対するフォールバック処理を確認します。

使用技術:
    - pytest によるテスト実行
    - conftest.py による storage_fixture の提供
"""

import json
from datetime import date
from pathlib import Path
from app.models.schemas import Prompt, Post

def test_save_and_load_post(storage_fixture):
    """
    投稿データを保存し、正しく読み込めることを確認するテスト。
    """
    prompt = Prompt(theme="記憶", genre="SF", setting="宇宙船の中")
    post = Post(
        date=date(2025, 7, 10),
        prompt=prompt,
        content="彼は記憶を失った状態で目を覚ました。",
        word_count=20
    )

    storage_fixture.save_post(post)
    loaded = storage_fixture.load_posts()

    assert "2025-07-10" in loaded
    assert loaded["2025-07-10"]["prompt"]["theme"] == "記憶"
    assert loaded["2025-07-10"]["content"].startswith("彼は記憶を")

def test_load_posts_with_empty_file(storage_fixture):
    """
    空の JSON ファイルを読み込んだ場合に空の辞書が返ることを確認するテスト。
    """
    storage_fixture.data_path.write_text("")  # 空ファイルを作成
    posts = storage_fixture.load_posts()
    assert posts == {}

def test_load_posts_with_invalid_json(storage_fixture):
    """
    壊れた JSON ファイルを読み込んだ場合に空の辞書が返ることを確認するテスト。
    """
    storage_fixture.data_path.write_text("{ invalid json }")  # 不正な JSON
    posts = storage_fixture.load_posts()
    assert posts == {}
