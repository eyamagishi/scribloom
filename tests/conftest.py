import pytest
from pathlib import Path
from app.services.storage import Storage

@pytest.fixture
def storage_fixture(tmp_path):
    """
    テスト用 Storage クラスのインスタンスを返す fixture。
    一時ディレクトリを使って安全な保存領域を提供する。
    """
    data_path = tmp_path / "posts.json"
    return Storage(data_path=data_path)
