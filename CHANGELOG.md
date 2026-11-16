# Changelog

This file records implemented changes. The displayed `v0.1.0` banner is not a
verified published release or tag.

## Unreleased

### Added

- Three standard-library entry-point tests for direct invocation, independent
  script execution, and silent import.
- An LF text line-ending policy in `.gitattributes`.
- A Windows Server 2025 / CPython 3.14.10 GitHub Actions test workflow with pinned
  official actions and no third-party project package installations.
- Windows setup, launch, and test instructions in the README.

### Changed

- Added a return type hint, function docstring, main guard, and final source-file
  newline to `main.py`; preserved the exact banner and `v0.1.0` version.
- Updated project evidence and remaining M1.3 acceptance gates.

### Validation status

See `PROJECT_STATUS.md` for Linux and Windows execution evidence. The owner-side
Windows runtime gate passed (3/3 tests). GitHub Actions execution and final
M1.3 acceptance remain pending.
