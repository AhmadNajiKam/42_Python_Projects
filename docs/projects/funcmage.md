# FuncMage

**Folder:** `FuncMage/`  
**Theme:** Functional programming — lambdas, higher-order functions, closures, decorators  
**Key file:** `decorator_mastery.py`

---

## Overview

FuncMage is a decorator-focused exercise framed around spellcasting. Each function models a real decorator pattern:

| Decorator | Pattern |
|---|---|
| `spell_timer` | Execution timing wrapper |
| `power_validator` | Input validation guard |
| `retry_spell` | Retry with exponential backoff |
| `MageGuild` | Class-based decorator with state |

---

## `spell_timer`

Wraps any callable and prints its execution time.

```python
import functools
import time

def spell_timer(func):
    """Measure and print the wall-clock time of a function call."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱  {func.__name__} executed in {elapsed:.6f}s")
        return result
    return wrapper
```

**Design notes:**

- Uses `time.perf_counter()` (not `time.time()`) for sub-millisecond precision.
- `functools.wraps` preserves `__name__` and `__doc__` — required by the exercise spec.
- Returns `result` so the decorator is transparent to callers.

---

## `power_validator`

Guards a function against out-of-range input.

```python
def power_validator(min_power: int, max_power: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if not (min_power <= power <= max_power):
                raise ValueError(
                    f"Power {power} out of range [{min_power}, {max_power}]"
                )
            return func(power, *args, **kwargs)
        return wrapper
    return decorator

@power_validator(min_power=1, max_power=100)
def cast_spell(power: int) -> str:
    return f"Spell at power {power}!"
```

**Design notes:** This is a *parametrised decorator* — a factory that returns a decorator. The three-level nesting (`power_validator` → `decorator` → `wrapper`) is the standard pattern.

---

## `retry_spell`

Retries a failing function up to `n` times with optional delay.

```python
import time
import functools

def retry_spell(max_attempts: int = 3, delay: float = 0.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator
```

**Design notes:** Re-raises the *last* exception after all attempts are exhausted so the caller gets a meaningful error rather than `None`.

---

## `MageGuild`

A class-based decorator that tracks how many times each spell has been cast.

```python
class MageGuild:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.cast_count = 0

    def __call__(self, *args, **kwargs):
        self.cast_count += 1
        print(f"🏰 Guild record: {self.func.__name__} cast {self.cast_count}x")
        return self.func(*args, **kwargs)

@MageGuild
def fireball():
    return "🔥"

fireball()   # Guild record: fireball cast 1x
fireball()   # Guild record: fireball cast 2x
print(fireball.cast_count)  # 2
```

**Design notes:** `functools.update_wrapper(self, func)` on a class instance is the equivalent of `@functools.wraps` for function decorators. It copies `__name__`, `__doc__`, `__module__`, and `__wrapped__` onto `self`.

---

## Lessons Learned

- **`functools.wraps` is non-negotiable.** Every decorator in a real codebase must preserve metadata — without it, `help()`, logging, and test introspection break.
- **Parametrised decorators have three levels of nesting** — factory, decorator, wrapper. It's easy to forget to `return wrapper` inside `decorator`.
- **Class-based decorators** are useful when you need to track state between calls. The trade-off is more boilerplate.
- **`time.perf_counter()`** is the right clock for benchmarking. `time.time()` can go backwards on NTP adjustments; `perf_counter` is monotonic.
