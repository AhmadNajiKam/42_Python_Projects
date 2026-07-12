# How to Debug with Python's Traceback

Read a Python traceback confidently and reach the root cause in under a minute.

---

## Anatomy of a Traceback

```
Traceback (most recent call last):        # (1) header — always present
  File "main.py", line 14, in <module>   # (2) outermost call
    result = cast_spell("fireball")
  File "spells.py", line 7, in cast_spell # (3) intermediate frames
    return SPELLS[name]()
KeyError: 'fireball'                      # (4) THE actual error — read this first
```

**Rule: read from the bottom up.**

1. The last line is the error type and message — this is your real clue.
2. The frame directly above it is where the error *occurred*.
3. Higher frames show how you got there.

---

## Step-by-Step: Isolate the Error

### Step 1 — Read the error type

| Error type | Likely cause |
|---|---|
| `TypeError` | Wrong argument type or count |
| `AttributeError` | Called `.something` on `None` or wrong type |
| `KeyError` | Dict key doesn't exist |
| `ValidationError` | Pydantic model received invalid input |
| `ImportError` | Module not found or circular import |
| `IndentationError` | Tabs mixed with spaces, or wrong indentation level |

### Step 2 — Go to the file and line

Open the file and line number from the bottom frame. Read the *actual line*, not just the error message.

### Step 3 — Print intermediate values

```python
def cast_spell(name: str):
    print(f"DEBUG: SPELLS keys = {list(SPELLS.keys())}")  # ← add this
    print(f"DEBUG: name = {repr(name)}")                  # ← and this
    return SPELLS[name]()
```

`repr()` reveals hidden characters: `repr("fireball ")` → `'fireball '` — there's a trailing space!

### Step 4 — Use `pdb` for complex state

```bash
python -m pdb main.py
```

Or insert a breakpoint directly:

```python
def cast_spell(name: str):
    breakpoint()          # drops you into pdb at this line (Python 3.7+)
    return SPELLS[name]()
```

Useful `pdb` commands:

| Command | Action |
|---|---|
| `n` | Execute next line |
| `s` | Step *into* a function call |
| `p expr` | Print the value of `expr` |
| `l` | List source around current line |
| `q` | Quit |

---

## Pydantic `ValidationError` Specifically

Pydantic errors are structured — don't just print the exception:

```python
from pydantic import ValidationError
from your_module import ContactLog

try:
    log = ContactLog(signal_id="BAD", frequency_mhz=-1)
except ValidationError as e:
    print(e.error_count(), "errors")
    for error in e.errors():
        print(f"  Field: {error['loc']}")
        print(f"  Message: {error['msg']}")
        print(f"  Input: {error['input']}")
```

Output:
```
2 errors
  Field: ('signal_id',)
  Message: Value error, signal_id must start with 'SIG-'
  Input: BAD
  Field: ('frequency_mhz',)
  Message: Value error, frequency_mhz must be positive
  Input: -1
```

---

## Quick Checklist

- [ ] Read the **last line** of the traceback first
- [ ] Identify the **file and line** in the bottom frame
- [ ] Add `print(repr(variable))` to check exact values
- [ ] Use `breakpoint()` if the state is complex
- [ ] For Pydantic errors, iterate `e.errors()` — not just `print(e)`
