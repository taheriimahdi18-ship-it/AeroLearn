# AeroLearn — Agent Instructions

These repository-wide instructions apply to coding agents and contributors working with AeroLearn. Read `PROJECT_STATUS.md` for current evidence and milestones. The project owner makes final decisions. Do not treat a roadmap item as authorization to implement it.

## 1. Project context

AeroLearn is an open-source Python aerospace engineering desktop application targeting Windows, developed with VS Code and Git/GitHub. It must be modular, scientifically accurate, maintainable and extensible. The planned GUI is PySide6; NumPy, SciPy and Matplotlib are planned only where needed. Verify compatibility before adoption. The exact package layout and supported Python versions are not yet finalized.

## 2. Workflow and scope

- Follow Plan → Implement → Test → Review → Commit → Document. Keep each task focused on one approved milestone.
- Before proposing changes, inspect the actual repository, current branch, commit, tracked files, working tree and relevant code. Compare with `PROJECT_STATUS.md`; report discrepancies rather than assuming the document is current.
- Preserve working, tested and approved features. Make minimal justified changes; do not refactor unrelated code. Explain the rationale, compatibility implications and risks before major architecture changes.
- Use Codex in ChatGPT on the web for coding assistance. The owner manually copies approved files into VS Code, validates on Windows and controls publication. Do not require an IDE extension.
- Never commit, push, open or merge a pull request, change repository settings or modify the owner's workspace without explicit task-specific approval. By default, work in the task's isolated environment only. Never force-push, reset or delete existing work as a shortcut. Stop and report unexpected modifications or a mismatched baseline.
- Respect documentation-only and read-only tasks. Do not install dependencies or change source during such tasks.

## 3. Implementation quality

- Write code, paths, identifiers, comments and technical documentation in English. Communicate with the owner in Persian unless a task requests another language; technical reports for review may be in English.
- Assume the owner is a beginner in programming. Supply complete runnable file contents, exact repository-relative paths and explicit Windows PowerShell/VS Code copy-paste instructions. Never require the owner to fill in omitted functions. Mark new versus replacement files clearly.
- Prefer small, typed, documented and testable functions with clear interfaces. Keep scientific calculations independent from GUI and plotting code. Keep dependencies minimal; do not introduce new frameworks or package structures without approval.
- Verify Python and library compatibility (including Windows installation availability) before installing or recommending a dependency. Record versions, platform and setup commands. Do not assume the cloud runtime matches Windows. Do not declare a Python version supported on the basis of a trivial script alone.

## 4. Scientific correctness

- State physical quantities, SI units, conversion conventions, coordinate/sign conventions where relevant, assumptions, reference equations and sources, validity ranges and limitations.
- Define input validation and numerical behavior for invalid or out-of-domain inputs. Handle boundary cases and floating-point tolerances explicitly where relevant.
- Validate calculations against analytical solutions and independent authoritative reference cases where available; test invariants, boundary cases and invalid inputs. Do not validate a formula only by duplicating the same implementation in a test.
- Never fabricate scientific results, sources or test outputs. Do not claim that an unexecuted test passed, that a historical draft is integrated, or that software is error-free. AeroLearn is not a certified operational aerospace tool.

## 5. Tests and review

- Include appropriate automated tests with each functional change; preserve existing tests. Run relevant tests and report exact commands, actual outputs or summaries, counts, exit codes, platform, interpreter and failures. If execution is unavailable, say so and provide a reproducible command.
- Distinguish smoke tests, unit tests, scientific validation and GUI/Windows acceptance. Cloud success is not Windows acceptance. Do not mark a feature complete until its acceptance criteria are evidenced.
- Before handoff, review the diff and list every changed file, explain what changed and why, provide launch/test instructions and a proposed commit message. The owner reviews before committing or pushing.

## 6. Documentation and security

- Keep `PROJECT_STATUS.md` current after approved milestones, with evidence and unresolved risks; maintain a clear roadmap, changelog and versioning strategy as the project grows. Do not confuse document revisions, a displayed banner version and actual software releases.
- GitHub is the source of truth for committed project code. Do not assume untracked local files or historic conversation drafts are in GitHub.
- Do not request, expose or store credentials, tokens, private conversation links, personal account details or unnecessary machine-specific paths in public files. Do not broaden access beyond the task. Do not grant agents repository write permissions merely to read a public repository.
- If instructions conflict, evidence is missing or an architectural change is needed, report the conflict and seek owner review instead of guessing or silently proceeding.
