# frontend/main.py

import streamlit as st
from datetime import date
from app.core.prompt import generate_daily_prompt
from app.models.schemas import Prompt, Post
from app.services.storage import save_post, load_posts

st.title("Scribloom ✍️")
st.subheader("本日のお題")

prompt_data = generate_daily_prompt()
st.markdown(f"- **テーマ**: {prompt_data['theme']}")
st.markdown(f"- **ジャンル**: {prompt_data['genre']}")
st.markdown(f"- **舞台**: {prompt_data['setting']}")

text = st.text_area("ここに物語や記事を書いてください...", height=300)

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
# 📚 投稿履歴の表示機能（追加部分）
# -------------------------------
st.subheader("📚 投稿履歴")

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
