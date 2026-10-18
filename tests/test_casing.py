
import pytest

from textutils import capitalize_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", "Hello World"),
        ("HELLO WORLD", "Hello World"),
        ("multiple   spaces", "Multiple   Spaces"),
        ("", ""),
        ("123 hello", "123 Hello"),
        ("école française", "École Française"),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected
