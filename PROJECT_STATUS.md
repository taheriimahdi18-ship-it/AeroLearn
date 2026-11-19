# AeroLearn — Project Status

- Document revision: 3.5 (M2 technical closeout; owner acceptance by publication)
- Assessment date: 2026-11-19
- Repository: https://github.com/taheriimahdi18-ship-it/AeroLearn
- Verified M2 starting repository baseline: `main` at `0001a3f719b3b5d16424b925ae582098a7eaf31e`
- Historical M1.3 starting baseline: `c03d6782abe7296c837bf5c5b24795c8cc757c93`
- Historical pre-foundation source baseline: `ad8c6b13849bb462a1e632b834ebf5334eefa0fb`
- Historical published foundation commit: `10390b64aaa5078ccf542eb427b29fbc03939d24` (`main`)
- M1.3 CI evidence: [Tests #1, Windows Python 3.14](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43956947531/job/133613878750)
- Published M1.3 closeout and CI #2: `0001a3f719b3b5d16424b925ae582098a7eaf31e`, [Tests #2](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43961821943)
- M2 implementation commit and last observed remote `main`: `d75363678eef6d4f6ec3e004dfeb138b09d5b4c9`
- M2 CI evidence: [Tests #3](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676), [job log](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676/job/135758370798)
- Displayed prototype version: `v0.1.0` (not a verified tag or release)
- Current milestone: M2 — Dynamic Pressure Calculator (published; technical gates passed; closeout publication records owner acceptance). Next: M3 — Modular architecture and quality (planning only).

This is a public technical summary of the more detailed revision 2.5 audit. M0, M1.1, M1.2, and M1.3 have been accepted by the owner. The M1.3 closeout was published in `0001a3f719b3b5d16424b925ae582098a7eaf31e`; its older conditional publication statements are superseded by that commit and owner acceptance. The owner separately approved the M2 scientific plan and implementation scope. Revision 3.2 was the Codex implementation handoff. Revision 3.3 records an independent review, a narrow input-type correction within the approved contract, and actual Linux evidence. Revision 3.4 recorded owner-supplied Windows test evidence and was published with the M2 implementation. Revision 3.5 records the staged review, implementation publication and successful M2 CI. M2 technical acceptance criteria are satisfied for the recorded scope; owner approval and publication of this closeout record formal milestone acceptance. The detailed historical record remains outside the public repository.

## 1. Mission

AeroLearn is an open-source Python aerospace engineering desktop application in early development. The goal is a modular, maintainable, extensible and scientifically validated learning and analysis platform for students, researchers and engineers. Windows is the primary desktop target; VS Code, Git and GitHub are used for development. The project is not certified for safety-critical operational decisions.

## 2. Verified baseline and evidence

| Item | Status and evidence |
| --- | --- |
| Initial repository | Initial commit `310c038ed54a46fdb1dc91b15090d74305a2905e`; three tracked files inspected in a supplied ZIP snapshot |
| License | MIT, inspected in snapshot and confirmed in subsequent Codex audit |
| Source baseline | `ad8c6b13849bb462a1e632b834ebf5334eefa0fb` — Add initial AeroLearn entry point |
| Repository synchronization | Owner-side Git output after documentation push showed identical local HEAD and live remote main SHA (`f2d6f0e330e21923a7fe9923fffa6211866a6eec`), branch up to date, and clean working tree |
| M1.3 published foundation | Owner terminal screenshot: `main` and live remote `refs/heads/main` both at `10390b64aaa5078ccf542eb427b29fbc03939d24`; clean working tree after push. Commit subject: Establish minimal software foundation and baseline tests. |
| M1.3 starting baseline | Codex fetched `origin/main`, verified `c03d6782abe7296c837bf5c5b24795c8cc757c93`, and created an isolated checkout at that exact commit with a clean working tree before editing. The older `ad8c6b1` checkout was not used for implementation. |
| M2 starting baseline | Codex fetched and verified remote `main` at `0001a3f719b3b5d16424b925ae582098a7eaf31e`, read all required baseline files, and created a separate clean checkout at that exact commit. The three baseline tests passed before edits. |
| M2 published implementation | Owner terminal screenshots: local HEAD and live remote `refs/heads/main` both at `d75363678eef6d4f6ec3e004dfeb138b09d5b4c9`, clean working tree after successful push. Commit subject: Implement and validate dynamic pressure calculator. |
| Git | Git for Windows 2.56.1.windows.1 executed successfully in PowerShell |
| Windows environment | Windows 10 Pro 22H2, build 19045, x86-64; CPython 3.14.10 and 3.15.2 installed side by side; both standard GIL-enabled 64-bit builds; VS Code Python extensions present |
| Original source preservation | Original script copied to the clone without overwriting; source and destination SHA-256 matched |
| Codex web access | Initial public clone and audits succeeded. All six tracked files were inspected at the exact M1.3 starting baseline; `AGENTS.md` and this status document were read in full before implementation. |
| Codex authorization | Public read access demonstrated; dedicated environment and authenticated write access not established or required; second audit inspected fetched `origin/main` at `f2d6f0e`, while the Codex checkout remained at `ad8c6b1` |
| Documentation | Revision 2.6 and `AGENTS.md` were published in `f2d6f0e330e21923a7fe9923fffa6211866a6eec`. Revision 2.8 was published in `c03d6782abe7296c837bf5c5b24795c8cc757c93`. Revision 2.9 was the implementation handoff; revision 3.0 recorded Windows verification and was published with the foundation in `10390b64aaa5078ccf542eb427b29fbc03939d24`. Revision 3.1 was published in `0001a3f719b3b5d16424b925ae582098a7eaf31e` with a separate successful CI run. Revision 3.2 was the uncommitted Codex M2 handoff; revision 3.3 was the reviewed handoff; Revision 3.4 recorded Windows test evidence and was published in `d75363678eef6d4f6ec3e004dfeb138b09d5b4c9`. Revision 3.5 records M2 technical closeout and is intended for owner-approved documentation-only publication. |

Evidence is based on owner-supplied Git/PowerShell screenshots, the inspected initial ZIP, and the Codex web audit report. The M2 starting baseline was independently reported by Codex; the newer M2 implementation baseline was verified by the owner using live Git commands and CI screenshots. Direct remote access for the closeout review was unavailable. These observations are not a continuous guarantee of the current remote HEAD.

### Tracked files at the historical M1.3 starting baseline (`c03d6782`)

```text
AeroLearn/
├── .gitignore
├── AGENTS.md
├── LICENSE
├── PROJECT_STATUS.md
├── README.md
└── main.py
```

At that starting baseline, `main.py` printed a five-line banner and invoked `main()` unconditionally; the README was a short introduction. No tests, CI workflow, dependency manifests, packaging configuration, engineering calculations, GUI or additional application modules were tracked. The M1.3 changes described below are not part of that historical starting baseline; they were subsequently published in `10390b64aaa5078ccf542eb427b29fbc03939d24`.

### Published foundation tree

```text
AeroLearn/
├── .gitattributes
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── PROJECT_STATUS.md
├── README.md
├── main.py
└── tests/
    └── test_main.py
```

The ten-file tree is derived from the starting baseline and the four additions in the owner’s commit output. The local `.venv` and generated bytecode remain excluded.

### Published M2 tree

```text
AeroLearn/
├── .gitattributes
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── PROJECT_STATUS.md
├── README.md
├── aerolearn/
│   ├── __init__.py
│   └── aerodynamics/
│       ├── __init__.py
│       └── dynamic_pressure.py
├── docs/
│   └── science/
│       └── dynamic_pressure.md
├── main.py
└── tests/
    ├── test_main.py
    └── test_dynamic_pressure.py
```

The 15-file tree follows from the ten-file foundation and the five M2 additions shown in the owner’s staged and commit output. No local virtual environment or generated bytecode is tracked.

## 3. Test evidence

| Check | Environment | Observed or reported result |
| --- | --- | --- |
| `python main.py` | Owner Windows workspace; terminal reported Python 3.15.2 | Owner screenshot: expected banner, exit code 0 |
| `python main.py` | Codex web, Linux x86_64, Python 3.12.14 | Codex reported expected banner, exit code 0, empty stderr |
| `./.venv/Scripts/python.exe main.py` (PowerShell equivalent: `.\.venv\Scripts\python.exe main.py`) | Owner Windows workspace; CPython 3.14.10 in `.venv` | Owner screenshot: expected banner, exit code 0 |
| VS Code Run Python File in Terminal | Owner Windows workspace; selected `.venv` (3.14.10) | Owner screenshot: explicit virtual-environment executable, activated prompt, expected banner and return to prompt; no error displayed |
| Dynamic-pressure calculation | Published M2 implementation | Implemented; numerical and API tests passed in the reported Linux environments, owner Windows workspace and hosted Windows CI (see variant-specific evidence below); experimental validation is not claimed |
| M1.3 automated tests | Codex Linux x86-64, CPython 3.12.14 | Three tests passed, zero failures/errors/skips, exit code 0; see section 6 for the exact command |
| M1.3 script smoke test | Codex Linux x86-64, CPython 3.12.14 | `python main.py` printed the original banner and exited 0 |
| M1.3 independent review tests | Linux, standard system CPython 3.13.5 | Three tests passed, zero failures/errors/skips, exit code 0; script also exited 0 with original banner and empty stderr |
| Updated M1.3 files on Windows | Owner Windows 10 Pro 22H2 / CPython 3.14.10 in `.venv` | Owner screenshot: script exit code 0; all three tests passed in 0.150 seconds, no failures/errors/skips, exit code 0 |
| GUI and installer | Current implementation | Not implemented or validated |
| GitHub Actions | Hosted Windows job `Windows Python 3.14`; configured Windows Server 2025, CPython 3.14.10 x64 | Owner screenshots: Tests #1 succeeded; all three named tests reported `ok`, `Ran 3 tests in 0.054s`, `OK`; no skips/errors/failures reported. Exact runtime patch/build not visible in the collapsed identification step. |
| Published closeout CI #2 | Commit `0001a3f719b3b5d16424b925ae582098a7eaf31e` | Earlier public metadata and owner screenshots confirm success; owner log showed 3/3 in 0.055 seconds, `OK`. Exact runtime patch was not visible |
| Pre-M2 baseline tests | Codex Linux x86-64, CPython 3.12.14 | 3 tests passed in 0.028 seconds before source edits; no failures/errors/skips; exit code 0 |
| Final original M2 handoff suite | Codex Linux x86-64, CPython 3.12.14 | 13 methods passed in 0.036 seconds; no failures/errors/skips; exit code 0 |
| Reviewed M2 suite | Independent Linux x86-64, CPython 3.13.5 | 13 methods passed in 0.027 seconds after the type-identity correction; 105 named scientific subtests; no failures/errors/skips; exit code 0 |
| Reviewed M2 normal-result oracle | Independent Linux x86-64, CPython 3.13.5 | 5,000 deterministic exact-rational comparisons passed; maximum observed distance 1 ULP; exit code 0 |
| Independent M2 numerical/API checks | Codex Linux x86-64, CPython 3.12.14 | 39/39 passed; maximum observed distance for eight selected normal rational oracles was 1 ULP, within the four-ULP tolerance |
| M2 owner Windows suite | Previously verified Windows 10 Pro 22H2 / CPython 3.14.10 `.venv` | Owner screenshot dated 2026-11-19: `Ran 13 tests in 0.109s`, `OK`, exit code 0; no failures, errors or skips reported |
| M2 CI | Published commit `d75363678eef6d4f6ec3e004dfeb138b09d5b4c9`; hosted Windows, CPython 3.14.10 AMD64 | Owner screenshots: [Tests #3](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676/job/135758370798), 13/13 methods passed in 0.054 seconds, `OK`; no failures, errors or skips reported; workflow success |

The historical smoke and M1.3 unit tests establish the recorded console and import behavior. The M2 tests verify selected scientific references, properties, input contracts, and numerical boundaries on Linux, the owner Windows workspace and hosted Windows CI. These results support M2 technical acceptance for the tested scope; they do not establish exhaustive numerical accuracy, experimental validity, general Python version support, GUI compatibility, or release readiness.

### Historical unintegrated lesson

A dynamic-pressure calculator (`lesson1.py`) and `tests/test_lesson1.py` were drafted previously. The later draft uses `q = 0.5 * rho * V**2` with SI units, checks finite non-negative inputs, and includes seven unittest methods: reference case (1.225 kg/m³, 50 m/s, 1531.25 Pa), zero speed, zero density, quadratic speed scaling, negative density, negative speed, and non-finite inputs. A historical assistant reported seven successful tests; the source files and execution logs are not part of the verified Git baseline. Do not mark this feature complete or transfer the old draft without review. Scientific assumptions, reference sources, numerical limits, and reproducible tests remain required.

The M2 audit examined the non-shallow history reachable from `0001a3f719b3b5d16424b925ae582098a7eaf31e`: six commits, with neither lesson filename in any tracked tree. The original draft source remains unavailable and unvalidated. The newly reviewed M2 module does not reconstruct or retroactively validate it. Deleted or inaccessible branches and private drafts were not searched.

## 4. Architecture and development direction

- Use a modular Python architecture and separate the scientific core from presentation and plotting.
- Use explicit SI units internally, documented conversions, physical assumptions, validity ranges and reference equations.
- Planned GUI: PySide6. Planned numerical and plotting tools: NumPy, SciPy and Matplotlib, only as required and after compatibility verification.
- Use type hints, clear English technical documentation and independent automated tests. The unchanged M1.3 CI workflow has three successful recorded push-triggered runs, including the expanded 13-method M2 suite in Tests #3.
- Keep previously approved behavior unless a justified, reviewed change is needed.
- GitHub is the source of truth for committed source. Codex in ChatGPT on the web is the chosen coding workspace; the owner manually transfers approved complete files into VS Code, tests on Windows and controls Git publication.
- Follow repository agent instructions in `AGENTS.md`, now published in the repository.

The primary development interpreter is CPython 3.14.10 (standard GIL, Windows x86-64); the installed 3.15.2 interpreter remains a fallback candidate, not an approved full-stack target. M2 introduces the approved minimal `aerolearn.aerodynamics` regular package for an independent scalar scientific API. Packaging/distribution metadata, a minimum distribution Python version, third-party dependencies, and broader CI remain deferred. Scientific calculations stay independent of the unchanged console and future GUI.

## 5. Python environment decision and acceptance (M1.2)

### Recorded configuration

- Windows 10 Pro 22H2 (build 19045), x86-64.
- Primary development interpreter: CPython 3.14.10, 64-bit, standard build (Free-threaded: False; GIL enabled: True).
- Retained interpreter: CPython 3.15.2, 64-bit, standard GIL-enabled build. It is a fallback candidate, not a fully validated support target.
- Project-local `.venv`, created with `py -3.14 -m venv .venv`; pip 26.2.2 reported inside it. No third-party application dependencies were installed during this stage.
- VS Code selected `.venv\Scripts\python.exe` and ran `main.py` using that executable. The terminal activated the environment; its process-scoped PowerShell execution policy adjustment is not a permanent system-wide change.
- An initial attempt to run `.venv\Scripts\python.exe` failed with `CommandNotFoundException`. The owner verified that `.venv` did not exist, created it, and successfully reran the checks. No source repair was required.
- `git check-ignore -- .venv/` returned `.venv/` and `git status --short` showed no changes after the virtual-environment smoke test. The environment is local, not a deliverable to commit.

### Reproduction and verification (Windows PowerShell, repository root)

```powershell
py -0p
py -3.14 --version
py -3.15 --version
# Only create if .venv is absent; inspect any existing environment first.
if (-not (Test-Path .venv)) {
    py -3.14 -m venv .venv
}
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe -c "import sys; print('Virtual environment:', sys.prefix != sys.base_prefix)"
.\.venv\Scripts\python.exe main.py
$LASTEXITCODE
git check-ignore -- .venv/
git status --short
```

The owner observed Python 3.14.10, pip 26.2.2 inside `.venv`, `Virtual environment: True`, the expected banner, exit code 0, and the ignore rule. Select the virtual-environment interpreter using VS Code's `Python: Select Interpreter`, then use `Run Python File in Terminal`. Direct invocation does not require activation or changes to system execution policy.

### Dependency research and limitations

The second Codex audit (2026-11-16) reported Windows x86-64 wheel availability and compatible direct metadata for NumPy, SciPy, Matplotlib, PySide6, pytest and Ruff on ordinary CPython 3.14 and 3.15. It noted that Matplotlib's 3.15 classifier coverage lagged its wheel availability. These are agent-reported metadata findings, not independent Windows installation or runtime tests and not dependency pins. Full transitive resolution, Windows imports/DLL loading, Qt GUI execution, plotting and scientific validation were not performed. The audit environment was Linux x86-64 with Python 3.12.14; do not substitute its results for Windows acceptance. Some rendered upstream documentation was unavailable (HTTP 403/404); Codex reported using official tagged repository documents instead.

Adopt a zero third-party runtime-dependency baseline for M1.3. Use standard-library `unittest` initially and `math` when needed for scalar scientific computations. Introduce pytest, Ruff and scientific/GUI packages only with a reviewed need, compatibility check and actual tests. Record exact dependency versions and reproducible installation details when adopted. A Python 3.14-compatible Codex runtime is desirable for future tests; if unavailable, report the actual version and require Windows confirmation.

Windows 10 is an observed development environment, not a long-term product-support commitment. Its ordinary support has ended; security update eligibility and a future Windows 11 migration need review. Define the minimum supported Windows version and verify Qt support before GUI adoption.

The owner accepted M1.2 for the baseline console script and its environment. The corresponding revision 2.8 status update was published in `c03d6782abe7296c837bf5c5b24795c8cc757c93`. No full-stack or scientific support is claimed.

## 6. M1.3 implementation and acceptance evidence

### Published implementation

- Modified `main.py` with `main() -> None`, a concise docstring, a conventional main guard and a final source-file newline. The five-line banner, leading spaces, final output newline and displayed `v0.1.0` are preserved.
- Added exactly three `unittest` methods in `tests/test_main.py`: direct invocation, independent script execution, and silent import in a fresh process. Expected output is defined independently; child processes use `sys.executable`, explicit working directories, captured streams and timeouts.
- Added `.gitattributes` with `* text=auto eol=lf`; no broad renormalization or global Git configuration change was performed.
- Expanded README setup, launch and test instructions; added `CHANGELOG.md` with an Unreleased section.
- Added `.github/workflows/tests.yml` for Windows Server 2025, standard x64 CPython 3.14.10, read-only contents permission and a five-minute timeout. It installs no third-party project packages.
- Preserved `.gitignore`, `AGENTS.md` and `LICENSE` unchanged. No application package, `src` directory, packaging metadata, dependency manifest, scientific function or GUI was added.

### Actual Codex execution

Environment: CPython 3.12.14; Linux x86-64, kernel 6.18.57, glibc 2.41. Python 3.14 was not available in this Codex environment and was not installed. No external project dependencies were installed and no virtual environment was created by Codex.

Command executed from the isolated implementation checkout root:

```text
python -m unittest discover -s tests -p "test_*.py" -v
```

Observed result: 3 tests ran in 0.061 seconds; all 3 passed, with 0 failures, 0 errors, 0 skips and exit code 0. A separate `python main.py` smoke test printed the original banner and exited 0. The full execution output is included in the implementation handoff. These are Linux results, not Windows acceptance.

An independent handoff review repeated the same unittest discovery and script smoke test with Linux system CPython 3.13.5. All three tests passed in 0.040 seconds (exit code 0), and the script produced the expected banner with empty stderr and exit code 0. An initial attempt using the review environment’s managed interpreter produced unrelated spreadsheet-runtime startup diagnostics on stderr and failed two tests; the repeat with the standard system interpreter passed without modifying application or test code. This evidence is also Linux-only.

### Verified CI references

Official latest stable releases and their direct commit tag references were verified through the GitHub API and `git ls-remote`:

- [actions/checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1): `3d3c42e5aac5ba805825da76410c181273ba90b1`.
- [actions/setup-python v7.1.0](https://github.com/actions/setup-python/releases/tag/v7.1.0): `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`.

The official [Python versions manifest](https://github.com/actions/python-versions/blob/main/versions-manifest.json) lists stable `3.14.10` with the standard `python-3.14.10-win32-x64.zip` artifact. Reference and artifact verification alone does not establish a successful run; the subsequent owner-provided CI evidence is recorded below.

### Actual owner-side Windows verification

On 2026-11-17 (owner local date), the owner supplied a VS Code/PowerShell screenshot showing the updated script and tests executed using the existing `.venv` interpreter, CPython 3.14.10, on the previously verified Windows 10 Pro 22H2 environment. The script printed the expected final banner lines and exited 0.

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
$LASTEXITCODE
```

Observed result: `test_import_is_silent_and_exposes_main`, `test_main_prints_banner_and_returns_none`, and `test_script_execution_prints_banner_and_exits_successfully` each reported `ok`; `Ran 3 tests in 0.150s`, `OK`, exit code 0, with no failures, errors or skips reported. The owner-side `git diff --check` printed no errors for the unstaged tracked changes. Git status listed exactly the three approved modified files and four approved new files. Subsequent staged checks and publication are recorded below.

### Owner-side Git review and publication

- The staged whitespace check (`git diff --cached --check`) produced no diagnostics. The staged status and stat showed the seven approved files only (four added, three modified; 358 insertions and 32 deletions).
- `git ls-files --eol` showed LF in the index for all ten files. The existing working copies of `LICENSE` and `.gitignore` still used CRLF; no broad renormalization or global configuration change was needed.
- The owner committed `Establish minimal software foundation and baseline tests` and pushed to `main`. Owner terminal evidence showed identical local HEAD and live remote main SHA: `10390b64aaa5078ccf542eb427b29fbc03939d24`, with a clean working tree.

### Actual GitHub Actions verification

On 2026-11-17 (owner local date), the owner supplied screenshots of the successful [workflow run #1](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43956947531) and its [job log](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43956947531/job/133613878750).

- Trigger: push to `main`, commit `10390b6`; workflow `Tests` (`tests.yml`); job `Windows Python 3.14`.
- Workflow status: Success; total duration 18 seconds; job duration 14 seconds.
- Command shown in the log: `python -m unittest discover -s tests -p "test_*.py" -v`.
- All three tests (`test_import_is_silent_and_exposes_main`, `test_main_prints_banner_and_returns_none`, `test_script_execution_prints_banner_and_exits_successfully`) reported `ok`. The log showed `Ran 3 tests in 0.054s` and `OK`; no failures, errors or skips reported.
- The Python identification step succeeded but was collapsed in the supplied screenshot. The workflow configuration targets standard x64 CPython 3.14.10 on `windows-2025`; the exact runtime patch and build were not independently read from the log. The successful hosted Windows run is distinct from the separately verified Windows 10 owner environment.
- CI evidence is for the foundation commit, not a future documentation-only commit or every future run. Pull-request-triggered execution was configured but has not been demonstrated by this run.

### M1.3 acceptance gates

| Gate | Evidence status |
| --- | --- |
| Authorized implementation and baseline regression tests | Passed; seven-file implementation reviewed; Codex and independent Linux tests passed |
| Owner Windows runtime | Passed; 3/3 tests, zero exit code, recorded CPython 3.14.10 |
| Staged review and Git publication | Passed for the recorded commit; seven expected files, no whitespace diagnostics, clean local/remote synchronization |
| Published push-triggered CI | Passed; Tests #1, 3/3 tests, successful job and workflow |
| Owner closeout acceptance | Accepted; closeout revision 3.1 published in `0001a3f719b3b5d16424b925ae582098a7eaf31e` |

No scientific calculations, GUI, distribution installer, or third-party runtime validation is included in this acceptance.

### Independently verified second CI run

Public GitHub run and job metadata confirm [Tests #2](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/43961821943) completed successfully for closeout commit `0001a3f719b3b5d16424b925ae582098a7eaf31e`, triggered by a push to `main`. Its single `Windows Python 3.14` job, labeled `windows-2025`, and its interpreter-identification and test steps succeeded. Run #1 was independently confirmed successful for its own foundation commit. Raw logs were unavailable without authentication in the earlier audit; exact interpreter output and raw test counts were not independently read. The owner subsequently supplied the #2 test log: all three tests passed, `Ran 3 tests in 0.055s`, `OK`; exact runtime patch was not visible. Both successful runs predate M2, and neither verifies the M2 code.

## 7. M2 implementation, publication and verification

### Implemented scope

- Added `aerolearn/__init__.py`, `aerolearn/aerodynamics/__init__.py`, and the pure scalar `dynamic_pressure` API in `aerolearn/aerodynamics/dynamic_pressure.py`.
- Added exactly ten new methods in `tests/test_dynamic_pressure.py`, using named subtests, analytical references, exact binary cases, and independent Fraction-based normal-result oracles. The complete suite discovers 13 methods.
- Added [scientific documentation](docs/science/dynamic_pressure.md) and updated README, CHANGELOG, and this status record.
- Preserved all seven other baseline files unchanged: `main.py`, `tests/test_main.py`, `.github/workflows/tests.yml`, `AGENTS.md`, `LICENSE`, `.gitignore`, and `.gitattributes`. The console output and `v0.1.0` banner remain unchanged.
- No external dependencies, GUI, plotting, atmosphere, Mach, Pitot conversion, lift/drag, array API, packaging metadata, or production Fraction fallback were added.

The API computes `q = 0.5 * rho * V²` in Pa from explicit kg/m³ and m/s inputs describing the same local flow state. Exact built-in `int` and `float` types are accepted. Density is validated fully before speed; negativity is checked before integer conversion, and both inputs are validated before the positive-zero shortcut. Types, invalid values, input conversion overflow, result overflow, and positive-input underflow have the exact approved exception classes and messages.

The fixed `(m_rho * m_v) * m_v` mantissa order and `math.ldexp` scaling avoid intermediate exponent overflow and premature underflow. Nonzero subnormals are accepted. Mantissa rounding and endpoint classification remain approximate; no correct-rounding, arbitrary-precision, or universal four-ULP guarantee is claimed. The function has no console or file I/O and is not a compressible Pitot-pressure conversion.

### Actual Codex test evidence

Environment: CPython 3.12.14, Linux 6.18.57 x86-64, glibc 2.41. Python 3.14 was unavailable and was not installed. No external project packages or virtual environments were installed or created. The owner's Windows environment was not modified.

The same command ran before implementation and for the expanded suite:

```text
python -m unittest discover -s tests -p "test_*.py" -v
```

| Execution | Observed result |
| --- | --- |
| Clean approved baseline, before edits | 3 tests, 0.028 seconds, all successful, 0 failures/errors/skips, exit 0 |
| Initial expanded suite | 13 tests, 0.043 seconds, all successful, 0 failures/errors/skips, exit 0 |
| Final expanded suite after adding six explicit approved reference subcases | 13 tests, 0.036 seconds, all successful, 0 failures/errors/skips, exit 0 |

The original Codex handoff contained 103 named scientific subtests. The reviewed handoff contains 105 after two additional regression subcases. Every calculator call in those tests captures stdout and stderr. Valid results are checked for exact float type, finiteness, nonnegativity, and positive-zero sign where applicable. Error cases check exact exception classes and complete messages, including plain `ArithmeticError` rather than its `OverflowError` subclass.

### Independent numerical verification

A separate standard-library verification harness, outside the repository, checked the production function against rational references formed from the exact converted float values. It did not reuse the production mantissa/exponent algorithm. Actual result: 39 checks passed, 0 failed, exit 0, on the same Linux CPython 3.12.14 environment.

The checks comprised eight normal-result Fraction oracles, eight exact binary boundary/cancellation vectors, three canonical-zero vectors, four range-exception cases, fifteen input-contract cases, and one captured import/call I/O check. The largest observed normal-oracle distance was one ULP, within the approved four-ULP tolerance. For example, density `1.225` and speed `50` returned `1531.2500000000002 Pa`, one ULP from the rounded exact-float rational reference `1531.25 Pa`. This illustrates ordinary float rounding; no fixed decimal rounding is applied.

The complete baseline, expanded-suite, and independent verification logs are supplied in the original Codex implementation handoff. Those results refer to the original Codex files, before the independent review correction. These checks are deterministic numerical verification, not exhaustive proof, experimental validation, operational certification, or Windows acceptance.

### Independent handoff review (revision 3.3)

The independent review extracted the eight complete files from the Codex report and used
the previously delivered M1.3 foundation and closeout snapshots. The Git blob hashes of
the preserved `main.py` and `tests/test_main.py` matched the owner-provided staged
Git output (`a676a0cc7f9c990b29e0707453c53194a4cf9ecb` and
`1d734edb5dcb84f7a61d96d34b3eea7a0054910d`, respectively). Direct live GitHub
access in the review environment failed; owner-side confirmation and publication
were subsequently observed as described below.

Environment: standard CPython 3.13.5, Linux 6.18.57 x86-64, glibc 2.41.
The baseline passed 3/3 methods in 0.036 seconds; the extracted original M2
handoff passed 13/13 in 0.034 seconds. The review reproduced a strict-type
contract defect: a custom metaclass overriding class equality could pass the
tuple membership check despite not being a built-in `int` or `float`. The
review replaced that check with explicit identity comparisons and added a
regression subcase in each argument position within the existing type test.
No arithmetic, exception messages, public API, or protected files were changed.

After correction, the full suite passed 13/13 in 0.027 seconds, with no
failures, errors, or skips, exit code 0. The ten scientific methods now cover
105 named subtests. A separate deterministic check (seed 20261117) compared
5,000 positive normal-result cases across a broad binary exponent range with
exact `Fraction` references, measuring representable float distance. All
5,000 were within four ULPs; the maximum observed distance was one ULP
(exit code 0). This sampled check does not establish a universal error bound
or exact endpoint classification.

### Owner-side Windows M2 verification (revision 3.4)

On 2026-11-19, the owner supplied a VS Code PowerShell screenshot from the existing activated project `.venv` on the previously verified Windows 10 Pro 22H2 / CPython 3.14.10 development environment. The recorded suite result was:

```text
Ran 13 tests in 0.109s

OK
0
```

All 13 test methods passed (ten scientific methods and three preserved foundation methods), with no failures, errors or skips reported. The screenshot shows five expected new files and three modified documentation files, no unexpected tracked changes, and no output from `git diff --check` for the unstaged tracked diff. The screenshot does not show a fresh interpreter identification, the standalone API invocation output, or a fresh remote HEAD check. The recorded environment is based on the previously verified setup. The staged file identities were subsequently checked; a separate standalone API smoke output is not visible in the supplied screenshots. The passed reference-value and API tests provide direct calculation evidence. This is owner-supplied evidence, not an independently executed Windows test.

### Owner-side staged review and publication (revision 3.5)

On 2026-11-19, owner-supplied PowerShell screenshots showed the approved eight-file staged change (five added, three modified; 910 insertions and 48 deletions). `git diff --cached --check` showed no diagnostics. The preceding review matched the eight staged Git blob identities to the reviewed implementation and Windows-documentation bundles; the seven protected files were not modified. The three revision 3.4 documentation blob identities were also matched to the archived bundle during this closeout review.

The owner committed `Implement and validate dynamic pressure calculator` and pushed it to `main`. The post-push `git status` reported an up-to-date branch and clean working tree. `git rev-parse HEAD` and `git ls-remote origin refs/heads/main` both displayed `d75363678eef6d4f6ec3e004dfeb138b09d5b4c9`. This is the last observed published implementation baseline, not the hash of this subsequent documentation-only closeout.

### Actual M2 GitHub Actions verification (revision 3.5)

Owner-supplied screenshots on 2026-11-19 show [workflow run #3](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676) and its [job log](https://github.com/taheriimahdi18-ship-it/AeroLearn/actions/runs/44580173676/job/135758370798).

- Workflow: `Tests`; push to `main`; commit `d753636`; status Success; total duration 20 seconds.
- Job: `Windows Python 3.14`; succeeded in 15 seconds. The preserved workflow specifies `windows-2025` (hosted Windows Server, not the owner's Windows 10 installation).
- `Identify Python` displayed `Python 3.14.10 (tags/v3.14.10:b703b2c, Oct 25 2026, 17:36:52) [MSC v.1944 64 bit (AMD64)]`.
- `Run tests` executed `python -m unittest discover -s tests -p "test_*.py" -v`. Each of the ten scientific and three foundation methods reported `ok`.
- The log ended with `Ran 13 tests in 0.054s` and `OK`; no failures, errors or skips were reported. The successful step and job establish successful execution; a separate numeric exit-code line was not displayed.
- Evidence is from the owner-provided Git and CI screenshots, not an independently fetched raw log. The reported earlier 5,000-case Linux oracle check is separate from this CI run; CI does not execute that external harness.

### M2 acceptance gates

| Gate | Evidence status |
| --- | --- |
| Scientific specification, API and architecture | Reviewed and approved for the M2 scope |
| Implementation and independent numerical verification | Passed for the recorded cases; 13 methods and 5,000 sampled normal-result oracles after the independent correction |
| Owner Windows verification | Passed; 13/13, exit code 0 |
| Staged review and implementation publication | Passed; eight expected files, reviewed identities, clean synchronized `d753636` |
| Published CI verification | Passed; Tests #3, 13/13, Python 3.14.10 AMD64 |
| Final owner closeout | Technical gates passed; owner approval and publication of revision 3.5 record formal acceptance |

A separate owner-side standalone API smoke result was requested but not captured in the supplied evidence; the successful automated reference tests cover the calculation. This optional supplementary check is not a separate release or experimental validation gate. No M3 implementation is authorized by this closeout.

## 8. Open issues and risks

| Issue | Next action |
| --- | --- |
| M2 acceptance | Technical gates passed; implementation published and CI #3 successful; owner approval and closeout documentation publication record formal acceptance |
| CI scope | Three recorded push-triggered runs succeeded; #3 includes M2 with exact Python 3.14.10 AMD64 visible in owner screenshots. PR-triggered execution and broader matrices remain untested |
| Packaging metadata and application layout | Minimal scientific package approved for M2; build/distribution infrastructure and larger refactors remain deferred |
| Windows Python and Codex Python versions differ | M2 has Codex Linux CPython 3.12.14, independent Linux CPython 3.13.5, and owner Windows CPython 3.14.10 environment evidence; hosted M2 CI also passed with Python 3.14.10 AMD64 |
| Floating-point range and accuracy | Documented computed-result exceptions and subnormal behavior; no exact classification of all endpoint inputs or universal relative-error bound |
| Planned scientific/GUI dependencies not runtime-validated | Metadata reviewed by Codex; defer installation until required, verify full resolution and runtime behavior then |
| Windows 10 lifecycle and future Qt support | Review OS security support and Windows 11 migration; decide minimum OS before GUI work |
| `*.spec` ignored by `.gitignore` | Revisit only if PyInstaller is chosen for distribution |
| Git LF/CRLF conversion warnings during documentation staging | Explicit LF policy published; all index entries were LF; two unchanged working-copy files remained CRLF. No broad renormalization needed |
| Historical dynamic-pressure lesson unavailable | Original source and logs are absent from verified reachable history; keep it unvalidated and distinct from the new M2 implementation |
| No formal release or safety validation | Keep prototype and release claims separate |

Earlier Git availability, workspace synchronization and Python extension setup issues were resolved for the observed Windows workspace. Their detailed history is retained outside the public repository.

## 9. Roadmap

| Milestone | Scope and acceptance gate | Status |
| --- | --- | --- |
| M0 — Repository audit | Identify repository, compare baseline, verify clone, smoke test, push and read-only Codex access | Complete for recorded baseline |
| M1.1 — Documentation | Review and publish public status and agent rules; documentation-only diff and verified commit | Complete; verified push of `f2d6f0e` |
| M1.2 — Python environment | Inventory interpreters, verify compatibility, approve a target, establish reproducible virtual environment and smoke test | Accepted by owner; environment record published in `c03d6782` |
| M1.3 — Software foundation | Preserve console output, add safe import behavior, baseline tests, documentation, LF policy and minimal CI | Accepted; foundation `10390b6`, closeout `0001a3f`, Windows baseline tests and both historical CI runs succeeded |
| M2 — Dynamic Pressure Calculator | Independent scientific function, SI units, reference cases, physical limits, tests and Windows verification | Published in `d753636`; technical gates passed (13 methods on owner Windows and hosted CI, plus independent Linux verification); owner-approved closeout publication records final acceptance |
| M3 — Modular architecture and quality | Stabilize package boundaries, CI, versioning and changelog; verify reproducibility | Planned |
| M4 — GUI | Minimal PySide6 interface connected to validated core; Windows UI smoke test | Planned |
| M5 — Standard atmosphere | Authoritative model, documented altitude convention and domain, reference/boundary tests | Planned |
| M6 — Aerospace modules | Aerodynamics, fluid mechanics, thermodynamics, flight mechanics and plots; validate one module at a time | Planned |
| M7 — Distribution | Windows installer, contributor documentation, release notes, tag and fresh-machine verification | Planned |

## 10. Immediate next action

Reconfirm local HEAD and live remote `main` at `d75363678eef6d4f6ec3e004dfeb138b09d5b4c9` and a clean working tree before applying revision 3.5. Review and publish only the three closeout documentation files with owner approval; check the resulting push-triggered CI. This does not change the scientific implementation.

After M2 acceptance, start M3 with a read-only architecture and quality review of the exact published baseline. Evaluate minimal package boundaries, reuse of scientific validation, versioning, reproducibility and CI scope without unnecessary refactoring; propose acceptance criteria before implementing changes. GUI, plotting, atmosphere, Mach/Pitot conversion, lift/drag, vectorization, packaging, and third-party dependency adoption are not authorized by this M2 implementation.

## 11. Maintaining this document

Update after each meaningful milestone with date, branch and source commit, changed files, exact test commands and observed results, unresolved risks, decisions and next task. Distinguish owner evidence, agent reports and independently executed tests. Keep credentials, private chat details, personal paths and account information outside the public repository. Use `AGENTS.md` for stable development rules and this document for changing status; maintain changelog and roadmap without conflicting duplication. Document revision numbers are not software release versions.
