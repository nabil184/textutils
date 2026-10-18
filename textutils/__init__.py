
"""A lightweight Python library for text processing."""

from .casing import capitalize_words
from .transform import character_count, reverse, word_count
from .word_frequency import word_frequency

__all__ = [
    "word_count",
    "character_count",
    "reverse",
    "capitalize_words",
    "word_frequency",
]
