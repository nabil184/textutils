"""Tests for the reverse function."""

import pytest

from textutils import reverse


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", ""),
        ("abc", "cba"),
        ("Hello World", "dlroW olleH"),
        ("12345", "54321"),
        ("école", "elocé"),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected
