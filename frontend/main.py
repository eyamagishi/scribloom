"""
Scribloom の Streamlit フロントエンド。

このモジュールは、日替わりのお題に基づいて文章を執筆・保存し、
履歴を閲覧できる創作支援アプリの UI を構築します。

主な機能:
    - お題の表示（テーマ・ジャンル・舞台）
    - Markdown 対応の執筆エリアと文字数カウント
    - 投稿の保存と履歴表示（JSON形式）

使用技術:
    - Streamlit によるインタラクティブ UI
    - Pydantic によるデータスキーマ管理
    - JSON ファイルによるローカルストレージ
"""

import streamlit as st
from datetime import date
from app.core.prompt import generate_daily_prompt
from app.models.schemas import Prompt, Post
from app.services.storage import save_post, load_posts

st.title("Scribloom ✍️")

# アプリのメイン画面に2つのタブを作成
tab1, tab2 = st.tabs(["📝 今日のお題", "📚 投稿履歴"])

with tab1:
    st.subheader("本日のお題")

    # 今日のお題データを生成
    # Returns: dict with keys 'theme', 'genre', and 'setting'
    prompt_data = generate_daily_prompt()

    st.markdown(f"- **テーマ**: {prompt_data['theme']}")
    st.markdown(f"- **ジャンル**: {prompt_data['genre']}")
    st.markdown(f"- **舞台**: {prompt_data['setting']}")

    # ユーザーの入力領域を提供
    text = st.text_area("ここに物語や記事を書いてください...", height=300)

    # 現在の文字数を表示
    st.caption(f"現在の文字数: {len(text)} 文字")

    # 入力内容のMarkdownプレビュー
    with st.expander("プレビュー（Markdown形式）"):
        st.markdown(text)

    # 投稿内容を保存
    if st.button("保存する"):
        if not text.strip():
            st.warning("文章が空です。何か書いてから保存してください。")
        else:
            # PromptおよびPostオブジェクトを生成して保存
            prompt = Prompt(**prompt_data)
            post = Post(
                date=date.today(),
                prompt=prompt,
                content=text,
                word_count=len(text)
            )
            save_post(post)  # 投稿内容をストレージに保存
            st.success("投稿を保存しました！")

with tab2:
    st.subheader("投稿履歴")

    # 保存された投稿の読み込み
    posts = load_posts()

    if not posts:
        st.info("まだ投稿はありません。")
    else:
        # 日付の新しい順に投稿を表示
        for post_date in sorted(posts.keys(), reverse=True):
            post = posts[post_date]
            prompt = post["prompt"]
            content = post["content"]
            word_count = post["word_count"]

            # 過去投稿を展開形式で表示
            with st.expander(f"{post_date}｜{prompt['theme']} × {prompt['genre']} × {prompt['setting']}（{word_count}文字）"):
                st.markdown(content)
