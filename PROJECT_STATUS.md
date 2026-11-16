# AeroLearn — Project Status

- Document revision: 3.0 (M1.3 Windows verification; pre-publication record)
- Assessment date: 2026-11-17
- Repository: https://github.com/taheriimahdi18-ship-it/AeroLearn
- Verified starting repository baseline: `main` at `c03d6782abe7296c837bf5c5b24795c8cc757c93`
- Last committed source-code change at that baseline: `ad8c6b13849bb462a1e632b834ebf5334eefa0fb`
- M1.3 implementation commit: not created; owner review and publication pending
- Displayed prototype version: `v0.1.0` (not a verified tag or release)
- Current milestone: M1.3 — Software foundation (implemented locally; Windows tests passed; CI and final acceptance pending)

This is a public technical summary of the more detailed revision 2.5 audit, updated after the owner approved the M1.3 foundation plan. M0, M1.1, and M1.2 have been accepted by the owner. The detailed historical record should be retained separately, outside the public repository. This revision records local implementation evidence and remaining acceptance gates; it does not authorize publication by an automated agent.

## 1. Mission

AeroLearn is an open-source Python aerospace engineering desktop application in early development. The goal is a modular, maintainable, extensible and scientifically validated learning and analysis platform for students, researchers and engineers. Windows is the primary desktop target; VS Code, Git and GitHub are used for development. The project is not certified for safety-critical operational decisions.

## 2. Verified baseline and evidence

| Item | Status and evidence |
| --- | --- |
| Initial repository | Initial commit `310c038ed54a46fdb1dc91b15090d74305a2905e`; three tracked files inspected in a supplied ZIP snapshot |
| License | MIT, inspected in snapshot and confirmed in subsequent Codex audit |
| Source baseline | `ad8c6b13849bb462a1e632b834ebf5334eefa0fb` — Add initial AeroLearn entry point |
| Repository synchronization | Owner-side Git output after documentation push showed identical local HEAD and live remote main SHA (`f2d6f0e330e21923a7fe9923fffa6211866a6eec`), branch up to date, and clean working tree |
| M1.3 starting baseline | Codex fetched `origin/main`, verified `c03d6782abe7296c837bf5c5b24795c8cc757c93`, and created an isolated checkout at that exact commit with a clean working tree before editing. The older `ad8c6b1` checkout was not used for implementation. |
| Git | Git for Windows 2.56.1.windows.1 executed successfully in PowerShell |
| Windows environment | Windows 10 Pro 22H2, build 19045, x86-64; CPython 3.14.10 and 3.15.2 installed side by side; both standard GIL-enabled 64-bit builds; VS Code Python extensions present |
| Original source preservation | Original script copied to the clone without overwriting; source and destination SHA-256 matched |
| Codex web access | Initial public clone and audits succeeded. All six tracked files were inspected at the exact M1.3 starting baseline; `AGENTS.md` and this status document were read in full before implementation. |
| Codex authorization | Public read access demonstrated; dedicated environment and authenticated write access not established or required; second audit inspected fetched `origin/main` at `f2d6f0e`, while the Codex checkout remained at `ad8c6b1` |
| Documentation | Revision 2.6 and `AGENTS.md` were published in `f2d6f0e330e21923a7fe9923fffa6211866a6eec`. Revision 2.8 was published in `c03d6782abe7296c837bf5c5b24795c8cc757c93` — Document verified Python development environment. Its statements that publication was pending are superseded by that verified commit. Revision 2.9 was the implementation handoff. Revision 3.0 records the subsequent owner-side Windows verification; the M1.3 implementation commit has not yet been created. |

Evidence is based on owner-supplied Git/PowerShell screenshots, the inspected initial ZIP, and the Codex web audit report. The live baseline was verified by the owner at the time of the recorded push and independently reported by Codex; this is not a continuous guarantee of the current remote HEAD.

### Tracked files at the verified starting repository baseline

```text
AeroLearn/
├── .gitignore
├── AGENTS.md
├── LICENSE
├── PROJECT_STATUS.md
├── README.md
└── main.py
```

At that starting baseline, `main.py` printed a five-line banner and invoked `main()` unconditionally; the README was a short introduction. No tests, CI workflow, dependency manifests, packaging configuration, engineering calculations, GUI or additional application modules were tracked. The local M1.3 changes described below are not part of that committed starting baseline.

## 3. Test evidence

| Check | Environment | Observed or reported result |
| --- | --- | --- |
| `python main.py` | Owner Windows workspace; terminal reported Python 3.15.2 | Owner screenshot: expected banner, exit code 0 |
| `python main.py` | Codex web, Linux x86_64, Python 3.12.14 | Codex reported expected banner, exit code 0, empty stderr |
| `./.venv/Scripts/python.exe main.py` (PowerShell equivalent: `.\.venv\Scripts\python.exe main.py`) | Owner Windows workspace; CPython 3.14.10 in `.venv` | Owner screenshot: expected banner, exit code 0 |
| VS Code Run Python File in Terminal | Owner Windows workspace; selected `.venv` (3.14.10) | Owner screenshot: explicit virtual-environment executable, activated prompt, expected banner and return to prompt; no error displayed |
| Scientific calculations | Current tracked source | None implemented; no scientific validation run |
| M1.3 automated tests | Codex Linux x86-64, CPython 3.12.14 | Three tests passed, zero failures/errors/skips, exit code 0; see section 6 for the exact command |
| M1.3 script smoke test | Codex Linux x86-64, CPython 3.12.14 | `python main.py` printed the original banner and exited 0 |
| M1.3 independent review tests | Linux, standard system CPython 3.13.5 | Three tests passed, zero failures/errors/skips, exit code 0; script also exited 0 with original banner and empty stderr |
| Updated M1.3 files on Windows | Owner Windows 10 Pro 22H2 / CPython 3.14.10 in `.venv` | Owner screenshot: script exit code 0; all three tests passed in 0.150 seconds, no failures/errors/skips, exit code 0 |
| GUI and installer | Current implementation | Not implemented or validated |
| GitHub Actions | M1.3 workflow prepared locally | Execution pending owner-controlled publication |

The smoke tests establish only that the banner script ran in the recorded environments. The M1.3 unit tests establish the tested console and import behavior in the recorded Linux and Windows environments. These results do not establish general Python version support, scientific accuracy, GUI compatibility, or release readiness.

### Historical unintegrated lesson

A dynamic-pressure calculator (`lesson1.py`) and `tests/test_lesson1.py` were drafted previously. The later draft uses `q = 0.5 * rho * V**2` with SI units, checks finite non-negative inputs, and includes seven unittest methods: reference case (1.225 kg/m³, 50 m/s, 1531.25 Pa), zero speed, zero density, quadratic speed scaling, negative density, negative speed, and non-finite inputs. A historical assistant reported seven successful tests; the source files and execution logs are not part of the verified Git baseline. Do not mark this feature complete or transfer the old draft without review. Scientific assumptions, reference sources, numerical limits, and reproducible tests remain required.

## 4. Architecture and development direction

- Use a modular Python architecture and separate the scientific core from presentation and plotting.
- Use explicit SI units internally, documented conversions, physical assumptions, validity ranges and reference equations.
- Planned GUI: PySide6. Planned numerical and plotting tools: NumPy, SciPy and Matplotlib, only as required and after compatibility verification.
- Use type hints, clear English technical documentation and independent automated tests. A minimal GitHub CI workflow is configured in M1.3; its execution remains pending.
- Keep previously approved behavior unless a justified, reviewed change is needed.
- GitHub is the source of truth for committed source. Codex in ChatGPT on the web is the chosen coding workspace; the owner manually transfers approved complete files into VS Code, tests on Windows and controls Git publication.
- Follow repository agent instructions in `AGENTS.md`, now published in the repository.

The primary development interpreter is CPython 3.14.10 (standard GIL, Windows x86-64); the installed 3.15.2 interpreter is retained as a fallback candidate, not an approved full-stack support target. The exact package layout, minimum supported Python version for distribution, dependency versions, test tooling beyond initial standard-library tests, CI matrix and packaging backend are not finalized. The proposed sequence validates a small scientific core before GUI integration; later architecture decisions require explicit review.

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

### Completed local implementation

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

The official [Python versions manifest](https://github.com/actions/python-versions/blob/main/versions-manifest.json) lists stable `3.14.10` with the standard `python-3.14.10-win32-x64.zip` artifact. Reference and artifact verification does not establish that the workflow has run successfully.

### Actual owner-side Windows verification

On 2026-11-17 (owner local date), the owner supplied a VS Code/PowerShell screenshot showing the updated script and tests executed using the existing `.venv` interpreter, CPython 3.14.10, on the previously verified Windows 10 Pro 22H2 environment. The script printed the expected final banner lines and exited 0.

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
$LASTEXITCODE
```

Observed result: `test_import_is_silent_and_exposes_main`, `test_main_prints_banner_and_returns_none`, and `test_script_execution_prints_banner_and_exits_successfully` each reported `ok`; `Ran 3 tests in 0.150s`, `OK`, exit code 0, with no failures, errors or skips reported. The owner-side `git diff --check` printed no errors for the unstaged tracked changes. Git status listed exactly the three approved modified files and four approved new files; the new files still require a staged whitespace/diff review. No M1.3 commit, push, or CI run has been evidenced.

### M1.3 acceptance gates

1. Owner applied the seven authorized files in the existing Windows workspace; final staged review remains pending.
2. Windows runtime gate passed: updated script and three tests executed through `.venv` on the recorded Windows environment; three successes, no skips and exit code 0.
3. Owner reviews line endings, the complete diff and preserved files, then controls all commits and publication. No implementation commit or future hash is claimed here.
4. The published GitHub Actions workflow runs successfully; its run evidence is recorded separately from Windows 10 acceptance.
5. Owner accepts M1.3 after reviewing the evidence. Until then, M1.3 remains in progress.

## 7. Open issues and risks

| Issue | Next action |
| --- | --- |
| M1.3 Windows acceptance | Runtime gate passed on the recorded Windows 10 Pro / CPython 3.14.10 environment; final staged review and CI remain pending |
| CI execution pending | Workflow and references are prepared; record an actual successful run after owner-controlled publication |
| Packaging metadata and application layout | Intentionally deferred; retain the approved flat foundation until an implemented need justifies a new structure |
| Windows Python and Codex Python versions differ | Codex used the exact approved source baseline but ran Python 3.12.14; separate owner-side Windows Python 3.14.10 evidence has now been recorded |
| Planned scientific/GUI dependencies not runtime-validated | Metadata reviewed by Codex; defer installation until required, verify full resolution and runtime behavior then |
| Windows 10 lifecycle and future Qt support | Review OS security support and Windows 11 migration; decide minimum OS before GUI work |
| `*.spec` ignored by `.gitignore` | Revisit only if PyInstaller is chosen for distribution |
| Git LF/CRLF conversion warnings during documentation staging | Explicit LF policy added locally; review owner-side line endings and diff without broad renormalization |
| Historical dynamic-pressure lesson not integrated | Review and independently validate during M2 |
| No formal release or safety validation | Keep prototype and release claims separate |

Earlier Git availability, workspace synchronization and Python extension setup issues were resolved for the observed Windows workspace. Their detailed history is retained outside the public repository.

## 8. Roadmap

| Milestone | Scope and acceptance gate | Status |
| --- | --- | --- |
| M0 — Repository audit | Identify repository, compare baseline, verify clone, smoke test, push and read-only Codex access | Complete for recorded baseline |
| M1.1 — Documentation | Review and publish public status and agent rules; documentation-only diff and verified commit | Complete; verified push of `f2d6f0e` |
| M1.2 — Python environment | Inventory interpreters, verify compatibility, approve a target, establish reproducible virtual environment and smoke test | Accepted by owner; environment record published in `c03d6782` |
| M1.3 — Software foundation | Preserve console output, add safe import behavior, baseline tests, documentation, LF policy and minimal CI | Implemented locally; Linux and Windows tests passed; staged review, publication, CI and owner acceptance pending |
| M2 — Dynamic Pressure Calculator | Independent scientific function, SI units, reference cases, physical limits, tests and Windows verification | Next planned milestone; not implemented |
| M3 — Modular architecture and quality | Stabilize package boundaries, CI, versioning and changelog; verify reproducibility | Planned |
| M4 — GUI | Minimal PySide6 interface connected to validated core; Windows UI smoke test | Planned |
| M5 — Standard atmosphere | Authoritative model, documented altitude convention and domain, reference/boundary tests | Planned |
| M6 — Aerospace modules | Aerodynamics, fluid mechanics, thermodynamics, flight mechanics and plots; validate one module at a time | Planned |
| M7 — Distribution | Windows installer, contributor documentation, release notes, tag and fresh-machine verification | Planned |

## 9. Immediate next action

Review the complete staged M1.3 diff and line endings, reverify the local and remote baseline, and leave Git commits and publication under owner control. The Windows test results are recorded above. Record GitHub Actions results only after an actual published run. Do not mark M1.3 complete before the Windows, CI and owner acceptance gates are satisfied.

After M1.3 acceptance, plan M2 Dynamic Pressure Calculator: review physical quantities and SI units, assumptions, authoritative equations, validity ranges, invalid inputs, floating-point behavior and independent reference tests. The historical lesson draft is not integrated or accepted. Do not begin M2 implementation or install scientific/GUI dependencies without separate approval.

## 10. Maintaining this document

Update after each meaningful milestone with date, branch and source commit, changed files, exact test commands and observed results, unresolved risks, decisions and next task. Distinguish owner evidence, agent reports and independently executed tests. Keep credentials, private chat details, personal paths and account information outside the public repository. Use `AGENTS.md` for stable development rules and this document for changing status; maintain changelog and roadmap without conflicting duplication. Document revision numbers are not software release versions.
