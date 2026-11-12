
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.2.1] - 2026-11-06

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
- Automated PyPI publishing through GitHub Actions and Trusted Publishing
- Release tag and package version consistency check
- Distribution metadata validation with Twine
- Quality checks and tests before publishing
- Changelog and test files included in the source distribution

### Changed

- Improved word frequency handling of case and punctuation
- Exposed word_frequency through the public API
- Updated .gitignore for generated files
- Reorganized the library into subpackages
- Moved tests next to their corresponding modules
- Updated package discovery and pytest configuration
- Documented testing and CI workflows
- Renamed the distribution to textutils-nabil184 while keeping textutils imports
- Documented PyPI installation separately from local development
- Declared the MIT license explicitly in package metadata

## [0.1.0] - 2026-10-01

### Added

- Initial Python package structure
- word_count() utility
- character_count() utility
- reverse() utility
- capitalize_words() utility
- Project documentation
- MIT License
