
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Pre-commit hooks for Black and Ruff
- GitHub Actions continuous integration workflow
- Four CI environments across Ubuntu, macOS and Python versions

### Changed

- Reorganized the library into subpackages
- Moved tests next to their corresponding modules
- Updated package discovery and pytest configuration

### Added

- Word frequency utility contributed through a Pull Request
- Automated tests using pytest
- Parametrized tests for normal and edge cases
- Tests for expected exceptions
- Test coverage configuration with pytest-cov
- Black and Ruff development tools
- NumPy-style docstrings for public functions
- Development and testing instructions in the README

### Changed

- Improved word frequency handling of case and punctuation
- Exposed word_frequency through the public API
- Updated .gitignore for testing and build artifacts

## [0.1.0] - 2026-10-01

### Added

- Initial Python package structure
- word_count() utility
- character_count() utility
- reverse() utility
- capitalize_words() utility
- Project documentation
- MIT License
