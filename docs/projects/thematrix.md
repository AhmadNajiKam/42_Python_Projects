# TheMatrix

**Folder:** `TheMatrix/`  
**Theme:** Python typing — `Protocol`, structural subtyping, `TypeVar`, `Callable` annotations  
**Key file:** `matrix.py`

---

## Core Concepts

### `Protocol` — structural subtyping

Protocols define interfaces without inheritance. Any class that implements the required methods satisfies the protocol — no `class Foo(MyProtocol)` needed.

```python
from typing import Protocol

class Transformable(Protocol):
    def transform(self, value: int) -> int: ...

class Doubler:                   # does NOT inherit from Transformable
    def transform(self, value: int) -> int:
        return value * 2

def apply(t: Transformable, x: int) -> int:
    return t.transform(x)

apply(Doubler(), 5)  # ✅ type-checks — Doubler satisfies Transformable structurally
```

### `TypeVar` — generic functions

```python
from typing import TypeVar

T = TypeVar("T")

def identity(value: T) -> T:
    return value

identity(42)       # → int
identity("hello")  # → str
```

### `Callable` annotations

```python
from typing import Callable

def apply_twice(f: Callable[[int], int], x: int) -> int:
    return f(f(x))

apply_twice(lambda x: x + 1, 0)  # → 2
```

---

## Why Protocols over ABCs?

| | `Protocol` | `ABC` |
|---|---|---|
| Requires explicit inheritance | No ✅ | Yes |
| Works with third-party classes | Yes ✅ | No |
| Runtime `isinstance` check | With `@runtime_checkable` | Yes |
| Best for | Duck-typed interfaces | Enforced contracts |

---

## Lessons Learned

- **Protocols enable open systems** — you can define an interface that third-party code satisfies without modifying it.
- **`@runtime_checkable`** is needed for `isinstance(obj, MyProtocol)` at runtime, but adds a small overhead — prefer static type checking with `mypy`.
- **`TypeVar` needs a consistent name** — by convention, `T`, `K`, `V` are common; always name the variable the same as the string: `T = TypeVar("T")` not `T = TypeVar("Item")`.
