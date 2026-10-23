"""Utilities for counting word frequencies.

Original implementation inspired by:
https://www.geeksforgeeks.org/python/find-frequency-of-each-word-in-a-string-in-python/
"""

import re
from collections import Counter


def word_frequency(s: str) -> dict[str, int]:
    """Count the frequency of each word in a text.

    The comparison is case-insensitive and punctuation is ignored.

    Parameters
    ----------
    s : str
        The input text.

    Returns
    -------
    dict[str, int]
        A dictionary containing each word and its frequency.

    Raises
    ------
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> word_frequency("Hello hello world!")
    {'hello': 2, 'world': 1}
    >>> word_frequency("")
    {}
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    words = s.split()

    cleaned_words = []
    for word in words:
        cleaned_words.extend(re.findall(r"\b\w+\b", word.casefold()))

    words = cleaned_words
    freq = Counter(words)

    result = {}
    for w, c in freq.items():
        result[w] = c

    return result


# Usage example
if __name__ == "__main__":
    print(word_frequency("hello hello there"))
