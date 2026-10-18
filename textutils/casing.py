def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word.

    Parameters
    ----------
    text : str
        The input text.

    Returns
    -------
    str
        Text with each word capitalized.

    Examples
    --------
    >>> capitalize_words("hello world")
    'Hello World'
    >>> capitalize_words("hello open source")
    'Hello Open Source'
    >>> capitalize_words("")
    ''
    """
    return text.title()
