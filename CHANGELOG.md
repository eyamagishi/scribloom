# CHANGELOG

このプロジェクトは [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) の形式に従って変更履歴を記録しています。  
バージョン管理は [Semantic Versioning](https://semver.org/lang/ja/) に準拠します。

---

## [Unreleased] - v0.2.0 構想

### ✨ 新機能（予定）
- お題再生成機能（セッション毎に異なるプロンプト表示）
- 投稿編集モード（履歴の加筆・再投稿が可能）
- GPT による創作支援ヒント表示
- 履歴検索フィルタ（ジャンル・キーワード対応）
- ダークモード切替オプション
- 投稿傾向の統計表示（ジャンル比率・文字数推移）

### 🛠 改善・最適化
- pytest の共通 fixture を conftest.py に統合
- Mermaid による構成／処理図を docs/ に追加

### 📘 ドキュメント
- README に次期機能構想リンクを追加
- docs/roadmap.md の新規作成
- deployment.md に Streamlit Cloud 公開手順を記載

---

## [v0.1.0] - 2025-07-10

### 📌 初期公開版
- Markdownベースの執筆UI
- 日替わりプロンプト提示機能
- 履歴保存と再表示機能
- GitHub Pages による技術ドキュメント公開
- MIT ライセンスにて OSS として初回公開
