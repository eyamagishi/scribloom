"""
generate_daily_prompt 関数のテストモジュール。

このテストでは、日付に基づいて一貫性のある創作お題が生成されること、
かつ異なる日付でお題が変化することを確認します。

使用技術:
    - pytest によるテスト実行
    - conftest.py による fixed_date fixture の活用
    - monkeypatch による datetime.date.today の動的置換
"""

import datetime
from app.core.prompt import generate_daily_prompt

def test_prompt_is_deterministic_for_same_date(monkeypatch):
    """
    同じ日付では同じお題が生成されることを確認するテスト。
    """
    monkeypatch.setattr(
        datetime,
        "date",
        type("FixedDate", (datetime.date,), {"today": classmethod(lambda cls: cls(2025, 7, 15))})
    )

    prompt1 = generate_daily_prompt()
    prompt2 = generate_daily_prompt()
    assert prompt1 == prompt2

def test_prompt_varies_by_date(monkeypatch):
    """
    異なる日付では異なるお題が生成されることを確認するテスト。
    """
    monkeypatch.setattr(
        datetime,
        "date",
        type("DateA", (datetime.date,), {"today": classmethod(lambda cls: cls(2025, 7, 15))})
    )
    prompt_a = generate_daily_prompt()

    monkeypatch.setattr(
        datetime,
        "date",
        type("DateB", (datetime.date,), {"today": classmethod(lambda cls: cls(2025, 7, 16))})
    )
    prompt_b = generate_daily_prompt()

    assert prompt_a != prompt_b
