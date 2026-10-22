"""A lightweight Python library for text processing."""

from .casing import capitalize_words
from .counting import character_count, word_count, word_frequency
from .transform import reverse

__all__ = [
    "word_count",
    "character_count",
    "reverse",
    "capitalize_words",
    "word_frequency",
]