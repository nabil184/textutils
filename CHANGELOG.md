
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Word frequency utility contributed through a Pull Request
- Automated tests with pytest
- Parametrized tests for normal and edge cases
- Tests for expected exceptions
- Test coverage with pytest-cov
- Black and Ruff development tools
- NumPy-style docstrings for public functions
- Pre-commit hooks for Black and Ruff
- GitHub Actions continuous integration workflow
- Four CI environments using Ubuntu, macOS and Python 3.11/3.12

### Changed

- Improved word frequency handling of case and punctuation
- Exposed word_frequency through the public API
- Updated .gitignore for generated files
- Reorganized the library into subpackages
- Moved tests next to their corresponding modules
- Updated package discovery and pytest configuration
- Documented testing and CI workflows

## [0.1.0] - 2026-10-01

### Added

- Initial Python package structure
- word_count() utility
- character_count() utility
- reverse() utility
- capitalize_words() utility
- Project documentation
- MIT License
