import pytest

from textutils import character_count, word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world", 2),
        ("", 0),
        ("   ", 0),
        ("one   two\nthree", 3),
        ("bonjour le monde", 3),
        ("it's a test", 3),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", 0),
        ("Hello", 5),
        ("Hello World", 11),
        ("é", 1),
        ("\n\t", 2),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected
