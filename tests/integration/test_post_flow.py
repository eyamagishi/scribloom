from app.core.prompt import generate_daily_prompt
from app.models.schemas import Post
from app.services.storage import Storage
from datetime import date

def test_prompt_to_post_to_storage(tmp_path):
    """
    generate_daily_prompt → Post モデル化 → Storage 保存 → 読み出し の一連処理を統合的に検証する。

    テスト目的:
    - お題生成結果が Prompt モデルとして正しく構築されること
    - その Prompt を元に Post がバリデーションを通過して生成されること
    - Storage クラスを使って投稿を保存・読み出しできること
    - 読み出したデータの整合性（content, word_count）が保たれていること

    利用技術:
    - tmp_path による一時ファイル操作（pytest 標準機能）
    - Pydantic モデルによる構造チェック
    - ISOフォーマットの日付キーで保存結果を確認
    """
    # Setup
    storage = Storage(data_path=tmp_path / "posts.json")
    prompt = generate_daily_prompt()
    content = "今日は夢について書いてみた。"
    word_count = len(content)

    # Create post
    post = Post(
        date=date.today(),
        prompt=prompt,
        content=content,
        word_count=word_count
    )

    # Save post
    storage.save_post(post)

    # Load and verify
    loaded = storage.load_posts()
    key = date.today().isoformat()
    assert key in loaded
    assert loaded[key]["content"] == content
    assert loaded[key]["word_count"] == word_count
