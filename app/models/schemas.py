# app/models/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Dict

class Prompt(BaseModel):
    theme: str
    genre: str
    setting: str

class Post(BaseModel):
    date: date
    prompt: Prompt
    content: str
    word_count: int
