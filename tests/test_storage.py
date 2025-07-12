"""
storage モジュールの投稿保存・読み込み機能に関するテスト。

このテストでは、Post モデルの保存・読み込み処理が正しく動作すること、
および空ファイルや壊れた JSON に対するフォールバック処理を確認します。

使用技術:
    - pytest によるテスト実行
    - conftest.py による storage_fixture の提供
"""

import json
from app.models.schemas import Post
from app.services.storage import Storage

def test_save_and_load_post(storage_fixture):
    """
    投稿データを保存し、正しく読み込めることを確認する。
    """
    post = Post(
        date="2025-07-12",
        content="テスト投稿",
        prompt={"theme": "夢", "genre": "SF", "setting": "宇宙船の中"},
        word_count=5  # ← これを追加
    )
    storage_fixture.save_post(post)

    loaded = storage_fixture.load_posts()
    assert "2025-07-12" in loaded
    assert loaded["2025-07-12"]["content"] == "テスト投稿"

def test_load_posts_with_empty_file(storage_fixture):
    """
    空のファイルから読み込んだ場合、空の辞書が返ることを確認する。
    """
    storage_fixture.data_path.write_text("")
    assert storage_fixture.load_posts() == {}

def test_load_posts_with_invalid_json(storage_fixture):
    """
    不正な JSON が含まれている場合でも、例外を出さず空の辞書を返すことを確認する。
    """
    storage_fixture.data_path.write_text("{ invalid json }")
    assert storage_fixture.load_posts() == {}
