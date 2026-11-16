# AeroLearn

AeroLearn is an open-source Python aerospace engineering learning and analysis
project targeting a Windows desktop application.

## Current scope

The current foundation prints the original `v0.1.0` console banner and provides
three standard-library tests for direct invocation, script execution, and silent
import. Aerospace calculations, a GUI, plotting, and distribution installers are
planned but are not implemented.

There are no third-party project dependencies. The displayed banner version is
not evidence of a published release. See [PROJECT_STATUS.md](PROJECT_STATUS.md)
for implementation evidence, successful Windows baseline tests, and the first
successful GitHub Actions run.

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

## Tests

Use explicit discovery from the repository root:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
$LASTEXITCODE
```

The acceptance target is exactly three discovered tests, three successes, no
skips, and exit code `0`. These tests cover console behavior, not scientific
accuracy or GUI compatibility. Recorded results are in
[PROJECT_STATUS.md](PROJECT_STATUS.md).

The CI workflow uses Windows Server 2025, x64 CPython 3.14.10, and the same
standard-library test discovery. It installs no third-party project packages.
The first push-triggered [CI run](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43956947531)
succeeded for foundation commit `10390b6` (three tests passed). The interpreter
patch is specified by the workflow; the exact runtime identification output was
not visible in the supplied evidence. Hosted Windows evidence is separate from
the owner's Windows 10 verification. Future runs must be evaluated individually.

## Contributions and project records

Read [AGENTS.md](AGENTS.md) before proposing changes. Save text files as UTF-8
with LF line endings; `.gitattributes` defines the Git text line-ending policy.
See [CHANGELOG.md](CHANGELOG.md) for unreleased changes and
[PROJECT_STATUS.md](PROJECT_STATUS.md) for milestones and acceptance gates.

## License

AeroLearn is available under the [MIT License](LICENSE).
