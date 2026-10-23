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
