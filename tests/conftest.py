import pytest
from pathlib import Path
from datetime import datetime
from app.services import storage
from app.models.schemas import Post

class MockStorage:
    """
    投稿の保存・読み込みをモジュール関数で扱うためのラッパークラス。
    テスト用に DATA_PATH を一時ディレクトリへ切り替え可能。
    """
    def __init__(self, temp_dir: Path):
        self.data_path = temp_dir / "posts.json"
        storage.DATA_PATH = self.data_path  # モジュール内のグローバルを書き換え

    def save_post(self, post: Post):
        return storage.save_post(post)

    def load_posts(self) -> dict:
        return storage.load_posts()

@pytest.fixture
def storage_fixture(tmp_path):
    """
    テスト用ストレージラッパーを提供する fixture。
    一時ディレクトリに書き込むよう設定済み。
    """
    return MockStorage(tmp_path)
