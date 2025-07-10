# frontend/main.py

import streamlit as st
from datetime import date
from app.core.prompt import generate_daily_prompt
from app.models.schemas import Prompt, Post
from app.services.storage import save_post

st.title("Scribloom ✍️")
st.subheader("本日のお題")

prompt_data = generate_daily_prompt()
st.markdown(f"- **テーマ**: {prompt_data['theme']}")
st.markdown(f"- **ジャンル**: {prompt_data['genre']}")
st.markdown(f"- **舞台**: {prompt_data['setting']}")

text = st.text_area("ここに物語や記事を書いてください...", height=300)

if st.button("保存する"):
    prompt = Prompt(**prompt_data)
    post = Post(
        date=date.today(),
        prompt=prompt,
        content=text,
        word_count=len(text)
    )
    save_post(post)
    st.success("投稿を保存しました！")
