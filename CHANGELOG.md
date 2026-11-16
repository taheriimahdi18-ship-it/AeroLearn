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
- Updated project evidence and M1.3 closeout records.

### Validation status

See `PROJECT_STATUS.md` for Linux and Windows execution evidence. The owner-side
Windows runtime gate passed (3/3 tests). The first GitHub Actions run also
passed all three tests for foundation commit `10390b6`
([Tests #1](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43956947531)).
All M1.3 technical gates are evidenced; owner review and publication of the
closeout documentation record final acceptance. No scientific or GUI validation
is claimed.
