"""One-line summary of a pull request."""


def summarise(title: str, additions: int, deletions: int) -> str:
    """Return the title followed by the size of the change."""
    changed = additions + deletions
    noun = "line" if changed == 1 else "lines"
    return f"{title.strip()} ({changed} {noun} changed)"
