# How to Run Tests Locally

Run `pytest` against an exercise before submitting to catch failures early.

---

## Install pytest

```bash
pip install pytest pytest-cov
```

---

## Basic run

From the project root:

```bash
pytest                          # discover and run all tests
pytest ex00/                    # run tests only in ex00/
pytest -v                       # verbose: show each test name
pytest -x                       # stop at first failure
pytest -k "timer"               # run only tests whose name contains "timer"
```

---

## Running against a specific model with Pydantic

Some exercises validate that your models raise `ValidationError` correctly. Use `pytest.raises`:

```python
# test_models.py
import pytest
from pydantic import ValidationError
from your_module import ContactLog

def test_invalid_signal_id_raises():
    with pytest.raises(ValidationError):
        ContactLog(signal_id="NOPE", frequency_mhz=1420.4)

def test_negative_frequency_raises():
    with pytest.raises(ValidationError):
        ContactLog(signal_id="SIG-001", frequency_mhz=-1.0)
```

```bash
pytest test_models.py -v
```

---

## Coverage report

```bash
pytest --cov=. --cov-report=term-missing
```

Aim for ≥ 80% coverage before submitting. The `term-missing` flag shows exactly which lines aren't covered.

---

## Common failure patterns

| Symptom | Likely cause |
|---|---|
| `ModuleNotFoundError` | Wrong working directory; run from the project root |
| `ImportError: cannot import name X` | Typo in your class or function name |
| `ValidationError` on valid input | Field validator is too strict; check boundary conditions |
| All tests pass locally, fail at 42 | Python version mismatch; check `python --version` matches the subject |

---

## Using a `.env` file in tests

If your exercise uses `pydantic-settings` / `python-dotenv`:

```bash
# Create a test-specific .env
cp .env .env.test
# Edit .env.test with safe test values

# Run with the test env
ENV_FILE=.env.test pytest
```

Or override in `conftest.py`:

```python
# conftest.py
import os
import pytest

@pytest.fixture(autouse=True)
def set_test_env(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    monkeypatch.setenv("DEBUG", "true")
```
