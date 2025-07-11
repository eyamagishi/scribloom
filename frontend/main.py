# frontend/main.py

"""
Scribloom の Streamlit フロントエンド。

このアプリは、日替わりのお題に基づいて文章を執筆・保存し、
履歴を閲覧できる創作支援ツールです。

主な機能:
- お題の表示（テーマ・ジャンル・舞台）
- Markdown対応の執筆エリアと文字数カウント
- 投稿の保存と履歴表示
"""

import streamlit as st
from datetime import date
from app.core.prompt import generate_daily_prompt
from app.models.schemas import Prompt, Post
from app.services.storage import save_post, load_posts

st.title("Scribloom ✍️")

# -------------------------------
# 🎨 タブ切り替え
# -------------------------------
tab1, tab2 = st.tabs(["📝 今日のお題", "📚 投稿履歴"])

# -------------------------------
# 📝 タブ1：今日のお題
# -------------------------------
with tab1:
    st.subheader("本日のお題")

    prompt_data = generate_daily_prompt()
    st.markdown(f"- **テーマ**: {prompt_data['theme']}")
    st.markdown(f"- **ジャンル**: {prompt_data['genre']}")
    st.markdown(f"- **舞台**: {prompt_data['setting']}")

    text = st.text_area("ここに物語や記事を書いてください...", height=300)

    # 🔢 文字数カウント
    st.caption(f"現在の文字数: {len(text)} 文字")

    # 👁 プレビュー（Markdown形式）
    with st.expander("プレビュー（Markdown形式）"):
        st.markdown(text)

    if st.button("保存する"):
        if not text.strip():
            st.warning("文章が空です。何か書いてから保存してください。")
        else:
            prompt = Prompt(**prompt_data)
            post = Post(
                date=date.today(),
                prompt=prompt,
                content=text,
                word_count=len(text)
            )
            save_post(post)
            st.success("投稿を保存しました！")

# -------------------------------
# 📚 タブ2：投稿履歴
# -------------------------------
with tab2:
    st.subheader("投稿履歴")

    posts = load_posts()

    if not posts:
        st.info("まだ投稿はありません。")
    else:
        for post_date in sorted(posts.keys(), reverse=True):
            post = posts[post_date]
            prompt = post["prompt"]
            content = post["content"]
            word_count = post["word_count"]

            with st.expander(f"{post_date}｜{prompt['theme']} × {prompt['genre']} × {prompt['setting']}（{word_count}文字）"):
                st.markdown(content)
