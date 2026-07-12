# 42 Norminette & Style Rules

Python exercises at 42 are graded against **PEP 8** via `pycodestyle`. This page documents every rule that comes up repeatedly in submissions.

---

## Run the Linter

```bash
pip install pycodestyle
pycodestyle --max-line-length=79 your_file.py
```

Zero output = zero errors. Any output = fix before submitting.

---

## Rules That Come Up Most

### Line Length — E501

Max 79 characters per line.

```python
# ❌ Too long
result = some_function(argument_one, argument_two, argument_three, argument_four)

# ✅ Break using implicit continuation inside parentheses
result = some_function(
    argument_one,
    argument_two,
    argument_three,
    argument_four,
)
```

### Blank Lines Around Definitions — E302 / E303 / E301

```python
# ❌ Missing two blank lines before top-level function
def foo(): pass
def bar(): pass

# ✅ Two blank lines between top-level definitions
def foo():
    pass


def bar():
    pass


# ✅ One blank line between methods inside a class
class MyClass:
    def method_a(self):
        pass

    def method_b(self):
        pass
```

### Whitespace Around Operators — E225 / E228

```python
# ❌
x=1
y = x*2+1

# ✅
x = 1
y = x * 2 + 1

# Exception: default argument values — NO spaces
def func(x=1, y=2): ...     # ✅
def func(x = 1, y = 2): ... # ❌
```

### Trailing Whitespace — W291 / W293

Configure your editor to strip trailing whitespace on save. In Neovim/Vim:

```vim
autocmd BufWritePre * %s/\s\+$//e
```

### Comparison to `None` — E711

```python
# ❌
if x == None: ...
if x != None: ...

# ✅
if x is None: ...
if x is not None: ...
```

### Comparison to `True`/`False` — E712

```python
# ❌
if flag == True: ...
if flag == False: ...

# ✅
if flag: ...
if not flag: ...
```

### Import Order — E401 / E402

```python
# ✅ One import per line; stdlib before third-party before local
import os
import sys

import pydantic

from .models import ContactLog
```

---

## What 42 Graders Check Beyond `pycodestyle`

| Check | Details |
|---|---|
| **Filename** | Must match the subject exactly (case-sensitive) |
| **Forbidden imports** | Read the subject — some ban `os`, `sys`, `re`, etc. |
| **`__pycache__`** | Must not be committed |
| **`.env` secrets** | Must not be committed |
| **Executable bit** | Some subjects require `chmod +x` on scripts |
| **Shebang** | `#!/usr/bin/env python3` required in executable scripts |

---

## Editor Setup (Arch Linux / Neovim)

Install `pycodestyle` as a linter source for `null-ls` / `nvim-lint`:

```lua
-- nvim-lint config
require("lint").linters_by_ft = {
  python = { "pycodestyle" },
}
```

Or with `conform.nvim` for auto-format on save using `autopep8`:

```bash
pip install autopep8
```

```lua
require("conform").setup({
  formatters_by_ft = {
    python = { "autopep8" },
  },
  format_on_save = { timeout_ms = 500 },
})
```
