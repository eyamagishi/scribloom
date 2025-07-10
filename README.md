# ✍️ Scribloom

毎日のお題で創作を習慣にする、シンプルな創作支援アプリ。

## 🔗 公開デモ

👉 [https://scribloom-ezvsuisqzzsqncvzvbsevd.streamlit.app](https://scribloom-ezvsuisqzzsqncvzvbsevd.streamlit.app)

## 🚀 機能概要

- 日替わりのお題（テーマ・ジャンル・舞台）
- 投稿の保存と履歴表示
- Markdownプレビューと文字数カウント
- タブでUIを整理

## 🛠 セットアップ方法

```bash
poetry install
poetry run streamlit run frontend/main.py
```

## 🧪 テスト実行

```bash
poetry run pytest --cov=app tests/
```

## 📌 今後の展望

- 自動保存機能
- 履歴の検索・フィルタ
- お題の再生成
- ダークモード対応（将来的に）
