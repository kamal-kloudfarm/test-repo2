"""Project utilities."""

from datetime import timedelta

from python_ms.ms import parse_time


def ms_to_timedelta(ms: str) -> timedelta:
    """Convert milliseconds to a timedelta object."""
    return timedelta(milliseconds=parse_time(ms))
