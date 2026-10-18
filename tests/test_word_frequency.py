
import pytest

from textutils import word_frequency


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello hello world!", {"hello": 2, "world": 1}),
        ("Hi, hi!", {"hi": 2}),
        ("", {}),
        ("    ", {}),
        ("!!! ...", {}),
        ("A b A", {"a": 2, "b": 1}),
        ("hello\nHELLO", {"hello": 2}),
        ("Python-python", {"python": 2}),
        ("Café café", {"café": 2}),
        ("one TWO two;one", {"one": 2, "two": 2}),
    ],
)
def test_word_frequency(text, expected):
    assert word_frequency(text) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        None,
        123,
        ["hello"],
    ],
)
def test_word_frequency_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        word_frequency(invalid_input)
