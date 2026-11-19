# Changelog

This file records implemented changes. The displayed `v0.1.0` banner is not a
verified published release or tag.

## Unreleased

### Added

- The pure scalar `aerolearn.aerodynamics.dynamic_pressure.dynamic_pressure` API,
  using explicit SI units, strict input validation, and scaled floating-point
  arithmetic with documented range errors.
- Ten standard-library dynamic-pressure test methods covering analytical
  references, independent Fraction oracles, scaling, input validation, integer
  conversion, signed zero, and normal/subnormal boundaries.
- Scientific documentation for the equation, pressure distinctions, physical
  assumptions, complete API contract, numerical limits, and NASA references.
- Three standard-library entry-point tests for direct invocation, independent
  script execution, and silent import.
- An LF text line-ending policy in `.gitattributes`.
- A Windows Server 2025 / CPython 3.14.10 GitHub Actions test workflow with pinned
  official actions and no third-party project package installations.
- Windows setup, launch, and test instructions in the README.

### Changed

- Added a return type hint, function docstring, main guard, and final source-file
  newline to `main.py`; preserved the exact banner and `v0.1.0` version.
- Updated current test instructions to 13 methods and recorded M2 implementation
  evidence separately from accepted M0 and M1 milestones.
- Recorded the published M1.3 closeout and its second successful CI run.
- Recorded the M2 implementation publication and successful third CI run;
  revision 3.5 documents the technical closeout and next planned milestone.
- Independent M2 review: enforce exact built-in type identity rather than
  overloaded class equality; add regression subcases for both input positions.

### Validation status

M0, M1.1, M1.2, and M1.3 are accepted. Historical Windows baseline tests passed,
and both [Tests #1](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43956947531)
and [Tests #2](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43961821943)
succeeded for their respective pre-M2 commits.

Before M2 edits, the three baseline tests passed on Codex Linux / CPython
3.12.14. The final expanded suite passed 13/13 methods with no failures, errors,
or skips and exit code `0`. Separate independent numerical/API verification
passed 39/39 checks on the original Codex handoff. Independent review on Linux /
CPython 3.13.5 reproduced 13/13 before and after the type-identity correction;
the reviewed version also passed 5,000 deterministic normal-result rational
oracle checks (maximum observed distance: 1 ULP). See `PROJECT_STATUS.md` for
evidence and limitations.

On 2026-11-19, the owner Windows suite passed 13/13 methods in 0.109 seconds
with exit code `0` and no reported failures, errors or skips in the previously
verified CPython 3.14.10 `.venv`. The reviewed implementation was published in
`d75363678eef6d4f6ec3e004dfeb138b09d5b4c9`. Owner-supplied Git and CI screenshots show a clean synchronized
`main` and successful [Tests #3](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676/job/135758370798) on hosted Windows with Python 3.14.10
AMD64: 13/13 methods passed in 0.054 seconds, `OK`, with no failures, errors or
skips reported. M2 technical gates are satisfied; owner-approved closeout
publication records final acceptance. These numerical checks do not constitute
experimental validation or operational certification. No GUI validation is claimed.
