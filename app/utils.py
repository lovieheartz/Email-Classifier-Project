# app/utils.py

import re


def clean_text(text: str) -> str:
    """
    Normalize text by removing extra spaces and line breaks.
    """
    return re.sub(r'\s+', ' ', text).strip()
