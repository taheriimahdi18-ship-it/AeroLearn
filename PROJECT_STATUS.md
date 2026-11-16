# AeroLearn — Project Status

- Document revision: 2.6 (public repository edition)
- Assessment date: 2026-11-16
- Repository: https://github.com/taheriimahdi18-ship-it/AeroLearn
- Verified code baseline: `main` at `ad8c6b13849bb462a1e632b834ebf5334eefa0fb`
- Displayed prototype version: `v0.1.0` (not a verified tag or release)
- Current milestone: M1.1 — project documentation

This is a public technical summary of the more detailed revision 2.5 audit. The detailed historical record should be retained separately, outside the public repository. This revision describes observed evidence and proposed work; it does not authorize implementation or publication by an automated agent.

## 1. Mission

AeroLearn is an open-source Python aerospace engineering desktop application in early development. The goal is a modular, maintainable, extensible and scientifically validated learning and analysis platform for students, researchers and engineers. Windows is the primary desktop target; VS Code, Git and GitHub are used for development. The project is not certified for safety-critical operational decisions.

## 2. Verified baseline and evidence

| Item | Status and evidence |
| --- | --- |
| Initial repository | Initial commit `310c038ed54a46fdb1dc91b15090d74305a2905e`; three tracked files inspected in a supplied ZIP snapshot |
| License | MIT, inspected in snapshot and confirmed in subsequent Codex audit |
| Source baseline | `ad8c6b13849bb462a1e632b834ebf5334eefa0fb` — Add initial AeroLearn entry point |
| Repository synchronization | Owner-side Git output after push showed identical local HEAD and live remote main SHA, clean working tree |
| Git | Git for Windows 2.56.1.windows.1 executed successfully in PowerShell |
| Windows environment | Python version reported by terminal: 3.15.2, 64-bit; VS Code Python extension and related extensions present |
| Original source preservation | Original script copied to the clone without overwriting; source and destination SHA-256 matched |
| Codex web access | Read-only public clone at the verified code baseline reported successful; all four tracked files inspected; clean checkout reported |
| Codex authorization | Public read access demonstrated; dedicated environment and authenticated write access not established or required |
| Documentation | Owner screenshot shows revision 2.5 present locally as untracked `PROJECT_STATUS.md`. Revision 2.6 and `AGENTS.md` are prepared for review; placement, staging, commit and push of these revisions are not verified. |

Evidence is based on owner-supplied Git/PowerShell screenshots, the inspected initial ZIP, and the Codex web audit report. The live baseline was verified by the owner at the time of the recorded push and independently reported by Codex; this is not a continuous guarantee of the current remote HEAD.

### Tracked files at the verified code baseline

```text
AeroLearn/
├── .gitignore
├── LICENSE
├── README.md
└── main.py
```

`main.py` defines `main()`, prints a five-line banner/status message and invokes `main()` unconditionally. It contains no engineering calculations, GUI or external dependencies. `README.md` is a short introduction. No automated tests, CI workflows, dependency manifests, packaging configuration or additional application modules were tracked at this baseline.

## 3. Test evidence

| Check | Environment | Observed or reported result |
| --- | --- | --- |
| `python main.py` | Owner Windows workspace; terminal reported Python 3.15.2 | Owner screenshot: expected banner, exit code 0 |
| `python main.py` | Codex web, Linux x86_64, Python 3.12.14 | Codex reported expected banner, exit code 0, empty stderr |
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
- Follow repository agent instructions in `AGENTS.md` once reviewed and adopted.

The exact package layout, minimum supported Python version, dependency versions, test tooling beyond initial standard-library tests, CI matrix and packaging backend are not finalized. The proposed sequence validates a small scientific core before GUI integration; later architecture decisions require explicit review.

## 5. Open issues and risks

| Issue | Next action |
| --- | --- |
| `main()` runs on import; no trailing newline | Non-blocking; preserve baseline now and address in an approved implementation task |
| Minimal README | Document actual launch/setup steps and implemented scope in M1.3 |
| No tests, packaging metadata or CI | Establish minimal foundation incrementally; do not claim tests before execution |
| Windows Python and Codex Python versions differ | Inventory available interpreters; verify supported versions and official package/wheel compatibility before selecting the target or creating the environment |
| Python scientific dependencies not verified | No installation until compatibility and dependency plan are reviewed |
| `*.spec` ignored by `.gitignore` | Revisit only if PyInstaller is chosen for distribution |
| Historical dynamic-pressure lesson not integrated | Review and independently validate during M2 |
| No formal release or safety validation | Keep prototype and release claims separate |

Earlier Git availability, workspace synchronization and Python extension setup issues were resolved for the observed Windows workspace. Their detailed history is retained outside the public repository.

## 6. Roadmap

| Milestone | Scope and acceptance gate | Status |
| --- | --- | --- |
| M0 — Repository audit | Identify repository, compare baseline, verify clone, smoke test, push and read-only Codex access | Complete for recorded baseline |
| M1.1 — Documentation | Review and publish public status and agent rules; documentation-only diff and verified commit | In progress |
| M1.2 — Python environment | Inventory interpreters, verify compatibility, approve a target, establish reproducible virtual environment and smoke test | Planned |
| M1.3 — Software foundation | Approve minimal structure; improve entry point and README as needed; add and run baseline automated tests | Planned |
| M2 — Dynamic pressure | Independent scientific function, SI units, reference cases, physical limits, tests and Windows verification | Planned |
| M3 — Modular architecture and quality | Stabilize package boundaries, CI, versioning and changelog; verify reproducibility | Planned |
| M4 — GUI | Minimal PySide6 interface connected to validated core; Windows UI smoke test | Planned |
| M5 — Standard atmosphere | Authoritative model, documented altitude convention and domain, reference/boundary tests | Planned |
| M6 — Aerospace modules | Aerodynamics, fluid mechanics, thermodynamics, flight mechanics and plots; validate one module at a time | Planned |
| M7 — Distribution | Windows installer, contributor documentation, release notes, tag and fresh-machine verification | Planned |

## 7. Immediate next action

Review the public `PROJECT_STATUS.md` and `AGENTS.md` locally, then review a documentation-only Git diff before any commit. Confirm that the remote baseline has not changed and that no source changes are included. After owner approval and verified publication, proceed to a read-only inventory of Python interpreters for M1.2. Python 3.12 is a candidate, not an adopted target. Do not install dependencies, refactor `main.py` or begin scientific implementation during M1.1.

## 8. Maintaining this document

Update after each meaningful milestone with date, branch and source commit, changed files, exact test commands and observed results, unresolved risks, decisions and next task. Distinguish owner evidence, agent reports and independently executed tests. Keep credentials, private chat details, personal paths and account information outside the public repository. Use `AGENTS.md` for stable development rules and this document for changing status; maintain changelog and roadmap without conflicting duplication. Document revision numbers are not software release versions.
