# Scribloom プロジェクト構造

このドキュメントでは、Scribloom のディレクトリ構成と各モジュールの責務を説明します。

## 🏁 ルートディレクトリ

- `README.md`: プロジェクト概要、使用方法、URL、今後の展望などを記載
- `pyproject.toml`: Poetry による依存管理と設定ファイル
- `poetry.lock`: lockされた依存関係
- `data/`: 投稿データを保存する永続ディレクトリ（`posts.json`）

## 🖥️ frontend/

Streamlit によるユーザーインターフェース層

- `main.py`: Scribloom の UI 実装。タブ構成で「お題の提示」と「履歴閲覧」を提供

## 🧠 app/

ドメインロジック、データ定義、サービス処理を格納

- `app/core/prompt.py`: 日付に基づいたお題生成ロジックを提供  
- `app/models/schemas.py`: 投稿とお題の Pydantic モデル定義  
- `app/services/storage.py`: 投稿データの保存・読み込みを JSON 形式で扱うモジュール

## 🧪 tests/

pytest によるユニットテスト群

- `test_prompt.py`: `generate_daily_prompt()` の日付ベースの変動性と再現性を検証  
- `test_storage.py`: 投稿の保存・読み込み処理とエラーケースを検証

## 🖼 images/

視覚的な補足資料（UIスクリーンショット等）

- `screenshot_ui.png`: Scribloom の画面イメージ。README で使用

## 🔧 __pycache__ / .pyc

Python のコンパイルキャッシュ。バージョン管理対象外（`.gitignore` 済み）

---

## 📦 開発ポリシー

- 各モジュールには PEP 257 に準拠した docstring を付与
- コミットメッセージは機能単位・目的別に構造化
- テストコードには各ケースの意図を docstring で明記

---

この構成により、Scribloom は保守性・可読性・拡張性の高い創作支援ツールとして運用されています。
