# Contributing

Thank you for your interest in contributing to **42 Python Projects**.

This repository contains Python exercises and projects completed as part of the 42 School curriculum. Contributions are welcome when they improve correctness, readability, documentation, testing, or educational value.

Please read [`CONVENTIONS.md`](CONVENTIONS.md) before contributing. This file explains the contribution workflow, while `CONVENTIONS.md` contains project-specific conventions.

## Development Setup

### Requirements

* Python 3.10 or newer
* Git
* `pip`
* A virtual environment is strongly recommended

### Clone the Repository

```bash
git clone https://github.com/AhmadNajiKam/42_Python_Projects.git
cd 42_Python_Projects
```

### Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

### Install Dependencies

Projects in this repository may have separate dependencies. Install the requirements for the specific project you are modifying:

```bash
python -m pip install -r requirements.txt
```

Run this command only when the relevant project contains a `requirements.txt` file.

To work on the documentation site:

```bash
python -m pip install -r docs-requirements.txt
mkdocs serve
```

## Running Tests and Checks

This repository contains multiple independent projects, so there is no single test command that applies to every directory. Follow the instructions provided by the relevant project or 42 subject.

### Subject-Provided Tests

If an exercise provides a test script or `main.py`, run it from the appropriate project directory:

```bash
python test.py
```

or:

```bash
python main.py
```

### Pytest

For projects that use `pytest`:

```bash
python -m pip install pytest pytest-cov
python -m pytest
```

Useful commands include:

```bash
python -m pytest -v
python -m pytest path/to/test_file.py
python -m pytest -x
python -m pytest -k "test_name"
python -m pytest --cov=. --cov-report=term-missing
```

### Style Checks

Python files should follow the repository’s style rules and the requirements of the relevant 42 subject.

Install and run `pycodestyle:

```bash
python -m pip install pycodestyle
pycodestyle --max-line-length=79 path/to/file.py
```

Before opening a pull request, verify:

* The relevant tests pass.
* The code follows `CONVENTIONS.md`.
* Filenames and output formats match the subject requirements.
* Forbidden imports have not been introduced.
* No `__pycache__`, `.pyc`, `.env`, secrets, or unrelated files are included.

## Reporting a Bug

Before filing a bug:

1. Search existing issues to ensure the problem has not already been reported.
2. Confirm that the behavior is not required by the relevant 42 subject.
3. Reproduce the issue using the latest version of the repository.

Create a bug report using the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).

A useful bug report should include:

* A clear description of the problem.
* The project or exercise affected.
* Exact steps to reproduce the issue.
* Expected behavior.
* Actual behavior.
* Operating system and Python version.
* Relevant traceback, logs, or screenshots.
* A minimal reproducible example when possible.

Do not include passwords, API keys, tokens, personal information, or other sensitive data in an issue.

## Pull Request Conventions

All changes must be submitted through a pull request. Do not commit directly to `main`.

### Branch Names

Create a focused branch from the latest `main` branch:

```bash
git switch main
git pull --ff-only origin main
git switch -c fix/short-description
```

Use one of the following prefixes:

* `feat/` — new functionality
* `fix/` — bug fix
* `docs/` — documentation changes
* `refactor/` — code restructuring without behavior changes
* `test/` — test-related changes

Examples:

```text
feat/add-validation-example
fix/handle-empty-input
docs/improve-testing-guide
refactor/simplify-parser
test/add-pydantic-tests
```

### Commit Messages

Use a concise, descriptive commit message:

```text
type(scope): short description
```

Examples:

```text
fix(FuncMage): handle empty input
docs: improve installation instructions
test(CosmicData): add invalid model cases
refactor: simplify exercise parser
```

### Pull Request Requirements

Before opening a pull request:

* Keep the pull request focused on one logical change.
* Do not mix unrelated refactoring with a feature or bug fix.
* Use the existing [pull request template](.github/PULL_REQUEST_TEMPLATE.md).
* Explain what changed and why.
* Reference related issues when applicable.
* Describe how the changes were tested.
* Update documentation when the behavior or usage changes.
* Remove generated files, temporary files, and secrets.
* Ensure the pull request targets `main`.

Use `Closes #123` only when the pull request completely resolves the referenced issue.

Complete alternative implementations should not be submitted unless they address a documented problem or provide a clear improvement to the project.

## Review Expectations

Reviewers evaluate pull requests based on:

* Correctness and expected behavior.
* Compliance with the relevant 42 subject.
* Adherence to `CONVENTIONS.md`.
* Test coverage and evidence of testing.
* Readability and maintainability.
* Scope and quality of the documentation.
* Absence of unrelated changes or sensitive files.

Review comments should be specific, constructive, and focused on the code or documentation rather than the contributor.

Contributors are expected to:

* Respond to substantive review comments.
* Explain design decisions when requested.
* Push revisions to the same branch.
* Re-run relevant tests after making changes.
* Resolve review discussions only after the underlying issue has been addressed.

A pull request may be rejected or requested for changes if it violates the subject requirements, lacks sufficient testing, contains unrelated changes, or does not provide enough information for effective review.

Pull requests must receive maintainer approval before merging. Contributors must not bypass review requirements or merge their own changes before approval.
