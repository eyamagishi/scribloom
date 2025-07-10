# tests/test_prompt.py

from app.core.prompt import generate_daily_prompt
import datetime

def test_prompt_is_deterministic_for_same_date(monkeypatch):
    # 2025-07-10 に固定
    class FixedDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2025, 7, 10)

    monkeypatch.setattr(datetime, "date", FixedDate)

    prompt1 = generate_daily_prompt()
    prompt2 = generate_daily_prompt()
    assert prompt1 == prompt2  # 同じ日付なら同じお題

def test_prompt_varies_by_date(monkeypatch):
    # 2025-07-10 に固定
    class DateA(datetime.date):
        @classmethod
        def today(cls):
            return cls(2025, 7, 10)

    # 2025-07-11 に固定
    class DateB(datetime.date):
        @classmethod
        def today(cls):
            return cls(2025, 7, 11)

    monkeypatch.setattr(datetime, "date", DateA)
    prompt1 = generate_daily_prompt()

    monkeypatch.setattr(datetime, "date", DateB)
    prompt2 = generate_daily_prompt()

    assert prompt1 != prompt2  # 日付が違えばお題も変わる
