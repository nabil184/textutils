# textutils

`textutils` is a lightweight Python library providing simple utilities for common text-processing operations.

## Features

The library currently provides:

- `word_count(text)` - Count the number of words in a text.
- `character_count(text)` - Count the number of characters in a text.
- `reverse(text)` - Reverse a text.
- `capitalize_words(text)` - Capitalize each word in a text.

## Installation

Clone the repository:

```bash
git clone https://github.com/nabil184/textutils.git
cd textutils
```

Install the package locally:

```bash
pip install -e .
```

## Usage

```python
from textutils import (
    word_count,
    character_count,
    reverse,
    capitalize_words,
)

text = "hello open source"

print(word_count(text))
print(character_count(text))
print(reverse(text))
print(capitalize_words(text))
```

Example output:

```text
3
17
ecruos nepo olleh
Hello Open Source
```

## Contributing

Contributions are welcome.

To contribute to the project, create a branch, make your changes, and submit them for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.