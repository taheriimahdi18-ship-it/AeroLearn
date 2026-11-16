# AeroLearn — Project Status

- Document revision: 2.8 (public repository edition; prepared locally, not yet committed)
- Assessment date: 2026-11-16
- Repository: https://github.com/taheriimahdi18-ship-it/AeroLearn
- Last verified repository baseline: `main` at `f2d6f0e330e21923a7fe9923fffa6211866a6eec`
- Last source-code change: `ad8c6b13849bb462a1e632b834ebf5334eefa0fb`
- Displayed prototype version: `v0.1.0` (not a verified tag or release)
- Current milestone: M1.3 — Software foundation (proposed next; implementation not started)

This is a public technical summary of the more detailed revision 2.5 audit, updated after publication of the initial project documentation. The detailed historical record should be retained separately, outside the public repository. This revision describes observed evidence and proposed work; it does not authorize implementation or publication by an automated agent.

## 1. Mission

AeroLearn is an open-source Python aerospace engineering desktop application in early development. The goal is a modular, maintainable, extensible and scientifically validated learning and analysis platform for students, researchers and engineers. Windows is the primary desktop target; VS Code, Git and GitHub are used for development. The project is not certified for safety-critical operational decisions.

## 2. Verified baseline and evidence

| Item | Status and evidence |
| --- | --- |
| Initial repository | Initial commit `310c038ed54a46fdb1dc91b15090d74305a2905e`; three tracked files inspected in a supplied ZIP snapshot |
| License | MIT, inspected in snapshot and confirmed in subsequent Codex audit |
| Source baseline | `ad8c6b13849bb462a1e632b834ebf5334eefa0fb` — Add initial AeroLearn entry point |
| Repository synchronization | Owner-side Git output after documentation push showed identical local HEAD and live remote main SHA (`f2d6f0e330e21923a7fe9923fffa6211866a6eec`), branch up to date, and clean working tree |
| Git | Git for Windows 2.56.1.windows.1 executed successfully in PowerShell |
| Windows environment | Windows 10 Pro 22H2, build 19045, x86-64; CPython 3.14.10 and 3.15.2 installed side by side; both standard GIL-enabled 64-bit builds; VS Code Python extensions present |
| Original source preservation | Original script copied to the clone without overwriting; source and destination SHA-256 matched |
| Codex web access | Read-only public clone at the verified code baseline reported successful; all four tracked files inspected; clean checkout reported |
| Codex authorization | Public read access demonstrated; dedicated environment and authenticated write access not established or required; second audit inspected fetched `origin/main` at `f2d6f0e`, while the Codex checkout remained at `ad8c6b1` |
| Documentation | Public revision 2.6 of `PROJECT_STATUS.md` and `AGENTS.md` reviewed, staged, committed and pushed successfully in `f2d6f0e330e21923a7fe9923fffa6211866a6eec` — Add project status and agent development guidelines. Owner output reported 152 insertions in two files and six tracked files after push. This revision 2.8 is a prepared update and has not been committed. |

Evidence is based on owner-supplied Git/PowerShell screenshots, the inspected initial ZIP, and the Codex web audit report. The live baseline was verified by the owner at the time of the recorded push and independently reported by Codex; this is not a continuous guarantee of the current remote HEAD.

### Tracked files at the last verified repository baseline

```text
AeroLearn/
├── .gitignore
├── AGENTS.md
├── LICENSE
├── PROJECT_STATUS.md
├── README.md
└── main.py
```

`main.py` defines `main()`, prints a five-line banner/status message and invokes `main()` unconditionally. It contains no engineering calculations, GUI or external dependencies. `README.md` is a short introduction. The documentation commit adds only agent instructions and project status; it does not modify `main.py`. No automated tests, CI workflows, dependency manifests, packaging configuration or additional application modules are tracked at the recorded baseline.

## 3. Test evidence

| Check | Environment | Observed or reported result |
| --- | --- | --- |
| `python main.py` | Owner Windows workspace; terminal reported Python 3.15.2 | Owner screenshot: expected banner, exit code 0 |
| `python main.py` | Codex web, Linux x86_64, Python 3.12.14 | Codex reported expected banner, exit code 0, empty stderr |
| `./.venv/Scripts/python.exe main.py` (PowerShell equivalent: `.\.venv\Scripts\python.exe main.py`) | Owner Windows workspace; CPython 3.14.10 in `.venv` | Owner screenshot: expected banner, exit code 0 |
| VS Code Run Python File in Terminal | Owner Windows workspace; selected `.venv` (3.14.10) | Owner screenshot: explicit virtual-environment executable, activated prompt, expected banner and return to prompt; no error displayed |
| Scientific calculations | Current tracked source | None implemented; no scientific validation run |
| Automated test suite | Current tracked source | No suite exists; no passing suite claimed |
| GUI, installer, CI | Current tracked source | Not implemented or validated |

These smoke tests establish only that the banner script ran in the recorded environments. They do not establish general Python version support, scientific accuracy, GUI compatibility, or release readiness.

### Historical unintegrated lesson

A dynamic-pressure calculator (`lesson1.py`) and `tests/test_lesson1.py` were drafted previously. The later draft uses `q = 0.5 * rho * V**2` with SI units, checks finite non-negative inputs, and includes seven unittest methods: reference case (1.225 kg/m³, 50 m/s, 1531.25 Pa), zero speed, zero density, quadratic speed scaling, negative density, negative speed, and non-finite inputs. A historical assistant reported seven successful tests; the source files and execution logs are not part of the verified Git baseline. Do not mark this feature complete or transfer the old draft without review. Scientific assumptions, reference sources, numerical limits, and reproducible tests remain required.

## 4. Architecture and development direction

- Use a modular Python architecture and separate the scientific core from presentation and plotting.
- Use explicit SI units internally, documented conversions, physical assumptions, validity ranges and reference equations.
- Planned GUI: PySide6. Planned numerical and plotting tools: NumPy, SciPy and Matplotlib, only as required and after compatibility verification.
- Use type hints, clear English technical documentation, independent automated tests and eventual GitHub CI.
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
py -3.14 -m venv .venv
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

M1.2 technical acceptance is complete for the baseline console script only; publication of this status update remains pending. No full-stack or scientific support is claimed.

## 6. Open issues and risks

| Issue | Next action |
| --- | --- |
| `main()` runs on import; no trailing newline | Non-blocking; preserve baseline now and address in an approved implementation task |
| Minimal README | Document actual launch/setup steps and implemented scope in M1.3 |
| No tests, packaging metadata or CI | Establish minimal foundation incrementally; do not claim tests before execution |
| Windows Python and Codex Python versions differ | Refresh Codex checkout to the approved baseline; prefer Python 3.14 for implementation tests if available, record actual environment and test on Windows |
| Planned scientific/GUI dependencies not runtime-validated | Metadata reviewed by Codex; defer installation until required, verify full resolution and runtime behavior then |
| Windows 10 lifecycle and future Qt support | Review OS security support and Windows 11 migration; decide minimum OS before GUI work |
| `*.spec` ignored by `.gitignore` | Revisit only if PyInstaller is chosen for distribution |
| Git LF/CRLF conversion warnings during documentation staging | Non-blocking; review an explicit `.gitattributes` policy during foundation work before changing line endings |
| Historical dynamic-pressure lesson not integrated | Review and independently validate during M2 |
| No formal release or safety validation | Keep prototype and release claims separate |

Earlier Git availability, workspace synchronization and Python extension setup issues were resolved for the observed Windows workspace. Their detailed history is retained outside the public repository.

## 7. Roadmap

| Milestone | Scope and acceptance gate | Status |
| --- | --- | --- |
| M0 — Repository audit | Identify repository, compare baseline, verify clone, smoke test, push and read-only Codex access | Complete for recorded baseline |
| M1.1 — Documentation | Review and publish public status and agent rules; documentation-only diff and verified commit | Complete; verified push of `f2d6f0e` |
| M1.2 — Python environment | Inventory interpreters, verify compatibility, approve a target, establish reproducible virtual environment and smoke test | Technical acceptance complete; status update publication pending |
| M1.3 — Software foundation | Approve minimal structure; improve entry point and README as needed; add and run baseline automated tests | Planned |
| M2 — Dynamic pressure | Independent scientific function, SI units, reference cases, physical limits, tests and Windows verification | Planned |
| M3 — Modular architecture and quality | Stabilize package boundaries, CI, versioning and changelog; verify reproducibility | Planned |
| M4 — GUI | Minimal PySide6 interface connected to validated core; Windows UI smoke test | Planned |
| M5 — Standard atmosphere | Authoritative model, documented altitude convention and domain, reference/boundary tests | Planned |
| M6 — Aerospace modules | Aerodynamics, fluid mechanics, thermodynamics, flight mechanics and plots; validate one module at a time | Planned |
| M7 — Distribution | Windows installer, contributor documentation, release notes, tag and fresh-machine verification | Planned |

## 8. Immediate next action

Review and publish this public status update through the owner's normal Git workflow. Then request a read-only M1.3 foundation plan from Codex after refreshing its checkout to the current approved remote commit and reading `AGENTS.md` and this document. Require a minimal change list, exact paths, preservation of the existing console output, a safe `__main__` guard, standard-library baseline tests, README setup/run/test instructions, and a proposed line-ending policy. Decide whether packaging metadata and a package layout belong in this milestone before implementing them. No scientific module, GUI, external dependency, commit, push or pull request is authorized by this plan alone. After approval, implement in the isolated coding environment, return complete files, run actual tests, and repeat them on Windows before owner-controlled publication.

## 9. Maintaining this document

Update after each meaningful milestone with date, branch and source commit, changed files, exact test commands and observed results, unresolved risks, decisions and next task. Distinguish owner evidence, agent reports and independently executed tests. Keep credentials, private chat details, personal paths and account information outside the public repository. Use `AGENTS.md` for stable development rules and this document for changing status; maintain changelog and roadmap without conflicting duplication. Document revision numbers are not software release versions.
