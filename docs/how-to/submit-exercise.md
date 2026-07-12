# How to Submit a 42 Exercise

This guide covers the exact steps from finishing your code to a clean push ready for peer review.

---

## Prerequisites

- Python ≥ 3.10 installed
- `git` configured with your 42 intra credentials
- The exercise repo cloned locally

---

## Steps

### 1. Check the exercise spec

Re-read the subject PDF one final time. Pay attention to:

- **Exact filenames** — 42 graders are case-sensitive.
- **Forbidden imports** — some exercises ban `import os`, `sys`, etc.
- **Expected output format** — trailing newlines, spacing, and encoding matter.

### 2. Lint with `pycodestyle`

42 Python exercises are graded against PEP 8. Run:

```bash
pycodestyle --max-line-length=79 your_file.py
```

Fix every reported issue before continuing. Common fixes:

| Error | Fix |
|---|---|
| `E302` | Add two blank lines before top-level functions/classes |
| `E501` | Break long lines; use implicit line continuation inside `()` |
| `W291` | Remove trailing whitespace |
| `E711` | Replace `== None` with `is None` |

### 3. Verify with the provided test script

If the subject includes a `test.py` or `main.py`:

```bash
python test.py
```

All assertions must pass silently. Any output means a failure.

### 4. Remove `__pycache__` and `.pyc` files

```bash
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete
```

Or add to your `.gitignore` (already done in this repo):

```gitignore
__pycache__/
*.pyc
*.pyo
.env
```

### 5. Stage only the required files

```bash
git add ex00/your_file.py   # add only what the subject asks for
git status                  # confirm nothing extra is staged
```

!!! danger "Never commit `.env` files"
    If your exercise uses `python-dotenv`, make sure `.env` is in `.gitignore` 
    before staging. Committing secrets is an automatic fail at 42.

### 6. Commit with a conventional message

```bash
git commit -m "feat(FuncMage): implement spell_timer decorator"
```

Format: `<type>(<scope>): <short description>`  
Common types: `feat`, `fix`, `refactor`, `docs`, `test`

### 7. Push

```bash
git push origin main
```

### 8. Verify on GitHub

Open the repo on GitHub and confirm:

- The correct files are present in the correct directories.
- No secrets, `__pycache__`, or unrelated files were pushed.
- The commit message is clean.

---

## Checklist

- [ ] Re-read the subject PDF
- [ ] `pycodestyle` reports zero errors
- [ ] Test script passes
- [ ] `__pycache__` removed
- [ ] `.env` not staged
- [ ] Only required files staged
- [ ] Conventional commit message written
- [ ] Pushed and verified on GitHub
