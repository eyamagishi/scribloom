import pytest
from datetime import date
from app.models.schemas import Post, Prompt
from app.services.storage import Storage

def test_empty_content(tmp_path):
    """
    content が空でも保存・読み込みできることを確認する。
    - 投稿内容が空文字列 "" のときも Storage に保存可能である
    - 読み込み後に空の内容が正しく保持されているか検証
    """
    storage = Storage(tmp_path / "posts.json")
    prompt = Prompt(theme="記憶", genre="SF", setting="宇宙船の中")

    post = Post(
        date=date.today(),
        prompt=prompt,
        content="",  # 空文字列コンテンツ
        word_count=0
    )
    storage.save_post(post)
    loaded = storage.load_posts()
    assert loaded[date.today().isoformat()]["content"] == ""

def test_word_count_mismatch(tmp_path):
    """
    word_count に不正な値（例: 負数）を与えた場合に ValidationError が発生することを確認する。
    - 実際の語数と一致しない場合の動作
    - Pydantic バリデーション（ge=0）によりエラーが発生することを検証
    """
    prompt = Prompt(theme="秘密", genre="ホラー", setting="廃墟となった図書館")

    with pytest.raises(ValueError):
        Post(
            date=date.today(),
            prompt=prompt,
            content="これは5語だけです。",
            word_count=-1  # 整合性に反する不正な値
        )

def test_prompt_accepts_dict(tmp_path):
    """
    Post の prompt に dict を渡した場合でも、自動的に Prompt モデルに変換されることを確認する。
    - Pydantic の構造的型変換が有効であることを検証
    - 誤って dict を渡した場合も整合性が保たれることを確認
    """
    storage = Storage(tmp_path / "posts.json")
    data = {
        "theme": "夢",
        "genre": "SF",
        "setting": "宇宙船の中"
    }

    post = Post(
        date=date.today(),
        prompt=data,  # dict → Prompt に自動変換
        content="これは有効なコンテンツです。",
        word_count=7
    )
    storage.save_post(post)

    loaded = storage.load_posts()
    key = date.today().isoformat()
    assert key in loaded
    assert loaded[key]["prompt"]["theme"] == "夢"
