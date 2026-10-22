
# textutils

`textutils` is a lightweight Python library providing simple
utilities for common text-processing operations.

## Features

The library currently provides:

- `word_count(text)` - Count the number of words in a text.
- `character_count(text)` - Count the number of characters.
- `reverse(text)` - Reverse a text.
- `capitalize_words(text)` - Capitalize each word.
- `word_frequency(text)` - Count how often each word appears.

## Installation

Clone the repository:

```bash
git clone https://github.com/nabil184/textutils.git
cd textutils
```

Install the package locally:

```bash
python -m pip install -e .
```

## Usage

```python
from textutils import (
    word_count,
    character_count,
    reverse,
    capitalize_words,
    word_frequency,
)

text = "hello open source"

print(word_count(text))
print(character_count(text))
print(reverse(text))
print(capitalize_words(text))
print(word_frequency("Hello hello world!"))
```

Expected output:

```text
3
17
ecruos nepo olleh
Hello Open Source
{'hello': 2, 'world': 1}
```

## Development

Install the development dependencies:

```bash
python -m pip install -e ".[dev]"
```

### Running tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run tests with coverage:

```bash
python -m pytest --cov=textutils --cov-branch --cov-report=term-missing
```

### Code quality

Format the project with Black:

```bash
python -m black .
```

Check formatting without modifying files:

```bash
python -m black --check .
```

Check code quality with Ruff:

```bash
python -m ruff check .
```

## Continuous Integration

This project uses GitHub Actions to automatically check
code quality and run the test suite.

The CI workflow runs on Pull Requests targeting `main`
and on pushes to `main`.

Four environments are tested:

- Ubuntu 22.04 with Python 3.11
- Ubuntu 22.04 with Python 3.12
- macOS 15 with Python 3.11
- macOS 15 with Python 3.12

Each CI job installs the project, checks Black and Ruff,
and executes pytest.

## Pre-commit

The project uses pre-commit to run Black and Ruff
automatically before commits.

Install the development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Install the Git hook:

```bash
python -m pre_commit install
```

Run all hooks manually:

```bash
python -m pre_commit run --all-files
```

## Tests

Tests are organized inside each package, close to
the corresponding implementation.

Run the full test suite:

```bash
python -m pytest -v
```

## Contributing

Contributions are welcome.

To contribute, create a branch, make your changes,
run the tests and open a Pull Request.

Please ensure that tests pass and that Black and Ruff
report no issues before submitting your changes.

## License

This project is licensed under the MIT License.
See the `LICENSE` file for details.
