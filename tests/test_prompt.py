"""
generate_daily_prompt 関数のテストモジュール。

このテストでは、お題生成が日付に依存して一貫性があり、
かつ日替わりで変化することを確認します。

使用技術:
    - pytest によるテスト実行
    - monkeypatch による datetime.date.today の動的置換
"""

from app.core.prompt import generate_daily_prompt
import datetime

def test_prompt_is_deterministic_for_same_date(monkeypatch):
    """
    同じ日付では同じお題が生成されることを確認するテスト。

    monkeypatch を使って datetime.date.today() を 2025-07-10 に固定し、
    同じ日に2度呼び出しても結果が一致することを確認します。
    """
    class FixedDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2025, 7, 10)

    monkeypatch.setattr(datetime, "date", FixedDate)

    prompt1 = generate_daily_prompt()
    prompt2 = generate_daily_prompt()
    assert prompt1 == prompt2  # 同じ日付なら同じお題

def test_prompt_varies_by_date(monkeypatch):
    """
    異なる日付では異なるお題が生成されることを確認するテスト。

    monkeypatch を使って datetime.date.today() を 2025-07-10 → 2025-07-11 に切り替え、
    お題が変化することを確認します。
    """
    class DateA(datetime.date):
        @classmethod
        def today(cls):
            return cls(2025, 7, 10)

    class DateB(datetime.date):
        @classmethod
        def today(cls):
            return cls(2025, 7, 11)

    monkeypatch.setattr(datetime, "date", DateA)
    prompt1 = generate_daily_prompt()

    monkeypatch.setattr(datetime, "date", DateB)
    prompt2 = generate_daily_prompt()

    assert prompt1 != prompt2  # 日付が違えばお題も変わる
