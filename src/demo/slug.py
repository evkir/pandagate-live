"""Slug for a pull request title."""

import re


def slugify(title: str) -> str:
    """Return the title lowercased, with other characters turned into dashes."""
    words = re.findall(r"[a-z0-9]+", title.lower())
    return "-".join(words)
