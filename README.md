# ✍️ Scribloom

**毎日のお題で創作を習慣にする、シンプルな創作支援アプリ。**  
日替わりのお題に沿って文章を書き、保存・振り返りができることで、創作を「続けられる」体験に変えます。

---

## 🔗 公開デモ

👉 [https://scribloom-ezvsuisqzzsqncvzvbsevd.streamlit.app](https://scribloom-ezvsuisqzzsqncvzvbsevd.streamlit.app)

> アプリはブラウザだけで起動し、インストール不要です。

---

## 🚀 主な機能

- 📅 日替わりのお題生成（テーマ・ジャンル・舞台）
- 📝 Markdown対応の執筆エリア（文字数カウント付き）
- 💾 投稿の保存と履歴表示（日付順に展開）
- 🧪 ユニットテスト完備（prompt / storage の正常系・異常系）

---

## 🖼️ スクリーンショット（任意）

> 使い方のイメージを伝えるために、アプリのUIを1〜2枚掲載すると効果的です。

```markdown
![Scribloom UI](images/screenshot_ui.png)
```

---

## 🛠 セットアップ方法

```bash
# Poetry を使って依存をインストール
poetry install

# アプリを起動
poetry run streamlit run frontend/main.py
```

> Python 3.10 以上が必要です。

---

## 🧪 テスト実行

```bash
poetry run pytest --cov=app tests/
```

> `pytest-cov` がインストールされていることを確認してください。

---

## 📁 ディレクトリ構成

```
.
├── app/           # アプリケーションのロジック
│   ├── core/      # お題生成
│   ├── models/    # スキーマ定義
│   └── services/  # ストレージ操作
├── frontend/      # Streamlit UI
├── data/          # 投稿データ（JSON）
├── tests/         # ユニットテスト
├── README.md
├── pyproject.toml
```

---

## 📌 今後の展望

- 💾 自動保存機能（下書きの保持と警告表示）
- 🔍 履歴の検索・フィルタ（キーワード・ジャンル）
- 🔁 お題の再生成機能
- 🌙 ダークモード対応
- 📣 フィードバックフォームの設置

---

## 🧑‍💻 開発者向けメモ

- 開発には Poetry を使用
- Streamlit Cloud に対応済み
- `.gitignore` にキャッシュ・秘密情報の除外設定あり
