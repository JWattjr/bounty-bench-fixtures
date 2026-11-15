"""Tiny slug helper used by the Bounty Bench live demo."""

import re


def normalize_slug(text: str) -> str:
    """Normalize basic ASCII text into a lowercase, hyphen-separated slug."""
    normalized = text.strip().lower()
    normalized = re.sub(r"\s+", "-", normalized)
    return re.sub(r"[^a-z0-9-]", "", normalized)

