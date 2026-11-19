# AeroLearn

AeroLearn is an open-source Python aerospace engineering learning and analysis
project targeting a Windows desktop application.

## Current scope

The console entry point preserves the original `v0.1.0` banner. The first
scientific API computes scalar dynamic pressure from explicit SI density and
relative flow speed. The suite contains three unchanged entry-point tests and
ten scientific test methods, using only the standard library.

M2 is published in commit [`d753636`](https://github.com/taheriimahdi18-ship-it/AeroLearn/commit/d75363678eef6d4f6ec3e004dfeb138b09d5b4c9).
The scientific suite passed on Codex Linux, in an independent Linux review, in
the owner Windows workspace, and in hosted Windows CI. Technical acceptance
gates are satisfied; owner-approved publication of the closeout documentation
records final milestone acceptance. M3 (modular architecture and quality) is
planned. GUI, plotting, atmospheric models, and distribution installers are not
implemented.

There are no third-party project dependencies. The displayed banner version is
not evidence of a published release. See [PROJECT_STATUS.md](PROJECT_STATUS.md)
for actual implementation evidence. Completed M0 and M1 milestones remain
accepted; their Windows and CI results do not validate the new M2 calculation.

## Development environment

- Primary development interpreter: standard CPython 3.14.10, x86-64, GIL enabled.
- Previously verified owner environment: Windows 10 Pro 22H2, build 19045.
- Editor: VS Code with the official Python extensions.
- Project-local virtual environment: `.venv`; recorded pip version: 26.2.2.
- CPython 3.15.2 is retained as a fallback candidate, not a validated support target.

A minimum Python or Windows version for distribution has not been finalized.
Codex Linux test results and GitHub-hosted Windows results are distinct from
acceptance on the owner's Windows 10 computer.

## Windows setup

For an existing checkout, open its folder in VS Code. For a new clone, run these
commands in PowerShell from the directory that should contain AeroLearn, then
open the cloned folder in VS Code:

```powershell
git clone https://github.com/taheriimahdi18-ship-it/AeroLearn.git
cd AeroLearn
```

Run the remaining commands from the repository root. Inventory the installed
interpreters and verify the primary version:

```powershell
py -0p
py -3.14 --version
```

If necessary, obtain the official
[Python 3.14.10 Windows 64-bit installer](https://www.python.org/downloads/release/python-31410/).
Use the standard GIL-enabled interpreter. Create `.venv` only when it is absent:

```powershell
if (-not (Test-Path .venv)) {
    py -3.14 -m venv .venv
}
```

Reuse the accepted environment. Inspect an existing environment rather than
deleting or recreating it. Verify it before running the project:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe -c "import sys, struct, sysconfig; print('Virtual environment:', sys.prefix != sys.base_prefix); print('Bits:', struct.calcsize('P') * 8); print('Free-threaded:', bool(sysconfig.get_config_var('Py_GIL_DISABLED')))"
git check-ignore -- .venv/
```

The accepted baseline is Python 3.14.10, `Virtual environment: True`, `Bits: 64`,
and `Free-threaded: False`. Stop and inspect any mismatch. No package installation
or pip upgrade is required.

In VS Code, run **Python: Select Interpreter** and select
`.venv\Scripts\python.exe`. Direct invocation below does not require activation
or a PowerShell execution-policy change. Never commit `.venv`.

## Launch

From the repository root:

```powershell
.\.venv\Scripts\python.exe main.py
$LASTEXITCODE
```

Expected application output:

```text
================================
       AeroLearn v0.1.0
 Aerospace Engineering Software
================================
Python environment is working!
```

The script should exit with code `0`. Importing `main` should produce no output.

## Dynamic-pressure API

From the repository root, use the canonical import:

```python
from aerolearn.aerodynamics.dynamic_pressure import dynamic_pressure

pressure_pa = dynamic_pressure(density_kg_m3=1.225, speed_m_s=100.0)
# Approximately 6125 Pa; no fixed decimal rounding is applied.
```

The function evaluates `q = 0.5 * rho * V²`, with density in kg/m³ and speed in
m/s for the same local flow state. It returns Pa, emits no output, and supplies
no default density or unit conversion. Exact built-in `int` and `float` inputs
must be finite and nonnegative; booleans and numeric subclasses are rejected.
Both inputs are validated before valid zero inputs return positive `0.0`.

The scaled calculation avoids intermediate exponent overflow and premature
underflow. Nonzero subnormals are accepted; final overflow and positive-input
underflow to zero raise explicit exceptions. Rounding remains approximate,
especially near floating-point endpoints. Dynamic pressure is not generally
equal to compressible Pitot impact pressure or stagnation-minus-static pressure.
Read the complete [scientific and API contract](docs/science/dynamic_pressure.md)
for physical assumptions, exact exceptions, numerical limits, and reference cases.

## Tests

Use explicit discovery from the repository root:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
$LASTEXITCODE
```

The current suite discovers exactly 13 methods: the three preserved console
tests and ten dynamic-pressure methods with named subtests. The Codex handoff run
on Linux / CPython 3.12.14 passed all 13 with no failures, errors, or skips and
exit code `0`. Independent review of the handoff reproduced that result, then
corrected an equality-based type check to use exact type identity and added two
regression subcases within the existing type-validation method. The reviewed
files passed all 13 methods on Linux / CPython 3.13.5 (105 scientific subtests,
exit code `0`). The owner Windows suite, using the previously verified CPython 3.14.10 `.venv`,
passed all 13 methods on 2026-11-19 in 0.109 seconds (exit code `0`; no failures,
errors or skips reported), as shown in the supplied terminal screenshot. Numerical references and boundary checks verify the calculation;
they do not establish experimental validity, sensor accuracy, or certification.
Recorded results are in [PROJECT_STATUS.md](PROJECT_STATUS.md).

The CI workflow uses Windows Server 2025, x64 CPython 3.14.10, and the same
standard-library test discovery. It installs no third-party project packages.
The first push-triggered [CI run](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43956947531)
succeeded for foundation commit `10390b6`. The second
[CI run](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43961821943)
succeeded for closeout commit `0001a3f`, the M2 starting baseline. Public metadata
confirmed both successes in the earlier audit; owner screenshots also show three
passing tests in each run. Neither historical run contains M2 changes. The third
[CI run](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676)
passed for M2 commit `d753636`. The owner-supplied [job log](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676/job/135758370798)
shows Python 3.14.10, AMD64 (64-bit), and all 13 tests passing in 0.054 seconds
with `OK`. Hosted Windows evidence remains separate from the owner's Windows 10
verification. PR-triggered CI and broader platform matrices remain unverified.

## Contributions and project records

Read [AGENTS.md](AGENTS.md) before proposing changes. Save text files as UTF-8
with LF line endings; `.gitattributes` defines the Git text line-ending policy.
See [CHANGELOG.md](CHANGELOG.md) for unreleased changes and
[PROJECT_STATUS.md](PROJECT_STATUS.md) for milestones and acceptance gates.

## License

AeroLearn is available under the [MIT License](LICENSE).
