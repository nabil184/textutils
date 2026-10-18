def word_count(text: str) -> int:
    """Count the number of words in a text.

    Parameters
    ----------
    text : str
        The input text.

    Returns
    -------
    int
        Number of words in the text.

    Examples
    --------
    >>> word_count("Hello Open Source")
    3
    >>> word_count("")
    0
    """
    return len(text.split())


def character_count(text: str) -> int:
    """Count the number of characters in a text.

    Parameters
    ----------
    text : str
        The input text.

    Returns
    -------
    int
        Number of characters, including spaces.

    Examples
    --------
    >>> character_count("Hello")
    5
    >>> character_count("Hello World")
    11
    """
    return len(text)


def reverse(text: str) -> str:
    """Reverse the characters in a text.

    Parameters
    ----------
    text : str
        The input text.

    Returns
    -------
    str
        Text with its characters in reverse order.

    Examples
    --------
    >>> reverse("Hello")
    'olleH'
    >>> reverse("")
    ''
    """
    return text[::-1]
