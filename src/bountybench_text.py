"""Small text and time helpers with three known bugs, used as live bounties."""

import re


def truncate_words(text: str, limit: int) -> str:
    """Keep at most `limit` words and add an ellipsis only if words were removed."""
    words = text.split()
    if len(words) <= limit:
        return text
    return " ".join(words[: limit - 1]) + "..."


def parse_duration(value: str) -> int:
    """Convert values like '1h30m', '45m' or '90s' into seconds."""
    match = re.match(r"(\d+)([hms])", value.strip().lower())
    if not match:
        raise ValueError("unsupported duration: " + value)
    amount, unit = int(match.group(1)), match.group(2)
    return amount * {"h": 3600, "m": 60, "s": 1}[unit]


def title_case(text: str) -> str:
    """Capitalize each word, keeping letters after an apostrophe lowercase."""
    return text.title()
