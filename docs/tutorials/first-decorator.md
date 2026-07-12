# Tutorial: Writing Your First Decorator

**Goal:** By the end of this tutorial you'll have written a working `spell_timer` decorator — exactly the kind required in the **FuncMage** project — and you'll understand *why* each line exists.

**Time:** ~20 minutes  
**Prerequisites:** Basic Python functions. No prior decorator knowledge needed.

---

## 1. What Problem Does a Decorator Solve?

Suppose you have several functions and you want to time all of them:

```python
import time

def cast_fireball():
    time.sleep(0.1)
    return "🔥 Fireball!"

# Naïve timing:
start = time.perf_counter()
result = cast_fireball()
end = time.perf_counter()
print(f"cast_fireball took {end - start:.4f}s")
```

That's fine for one function. For ten functions it becomes repetitive noise. A decorator lets you *wrap* that timing logic once and reuse it anywhere with a single `@` line.

---

## 2. Understanding Closures First

A decorator is a function that returns a function. That inner function is called a **closure** — it "closes over" variables from the outer scope.

```python
def make_greeter(greeting):  # (1)
    def greet(name):          # (2)
        return f"{greeting}, {name}!"  # (3)
    return greet              # (4)

hello = make_greeter("Hello")
print(hello("Ahmad"))  # → Hello, Ahmad!
```

1. `make_greeter` is a **factory** — it creates customised functions.
2. `greet` is defined *inside* `make_greeter` — it's the closure.
3. `greeting` is captured from the outer scope even after `make_greeter` returns.
4. We return the function object itself (no parentheses — don't call it!).

---

## 3. Your First Decorator

A decorator is just a closure factory where the outer argument is the *function being decorated*:

```python
def spell_timer(func):          # (1)
    def wrapper(*args, **kwargs):  # (2)
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)  # (3)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result               # (4)
    return wrapper                  # (5)
```

1. `func` is the function we're wrapping — passed in automatically by `@spell_timer`.
2. `wrapper` accepts any positional and keyword arguments with `*args, **kwargs` so it works with any function signature.
3. We call the *original* function and capture its return value.
4. Always return the result — callers expect it.
5. Return the `wrapper` closure, not the result of calling it.

Apply it with the `@` syntax:

```python
@spell_timer
def cast_fireball():
    import time
    time.sleep(0.1)
    return "🔥 Fireball!"

cast_fireball()
# cast_fireball took 0.1003s
```

!!! note "What `@spell_timer` actually does"
    `@spell_timer` above a `def` is exactly equivalent to writing:
    ```python
    cast_fireball = spell_timer(cast_fireball)
    ```
    It replaces `cast_fireball` with the `wrapper` closure returned by `spell_timer`.

---

## 4. Preserve the Function's Identity with `functools.wraps`

There's a problem with the decorator above:

```python
print(cast_fireball.__name__)  # → 'wrapper'  ❌
print(cast_fireball.__doc__)   # → None        ❌
```

The wrapper has replaced the original function's metadata. Fix this with `functools.wraps`:

```python
import functools
import time

def spell_timer(func):
    @functools.wraps(func)          # ← copies __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper
```

Now:

```python
@spell_timer
def cast_fireball():
    """Cast a powerful fireball spell."""
    time.sleep(0.1)
    return "🔥 Fireball!"

print(cast_fireball.__name__)  # → 'cast_fireball' ✅
print(cast_fireball.__doc__)   # → 'Cast a powerful fireball spell.' ✅
```

!!! warning "Always use `@functools.wraps`"
    Without it, introspection tools, test frameworks, and debuggers see `wrapper` 
    everywhere instead of your real function names. It's a one-liner with no downsides.

---

## 5. Chaining Decorators

You can stack multiple decorators — they apply **bottom-up**:

```python
def log_spell(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📜 Casting: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@spell_timer   # applied second (outermost)
@log_spell     # applied first (innermost)
def cast_fireball():
    time.sleep(0.05)
    return "🔥"
```

```
cast_fireball()
# 📜 Casting: cast_fireball
# cast_fireball took 0.0503s
```

---

## 6. Putting It All Together

Here's the final `spell_timer` as it appears in **FuncMage**:

```python
import functools
import time

def spell_timer(func):
    """Decorator that prints the execution time of the wrapped function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱  {func.__name__} executed in {elapsed:.6f} seconds")
        return result
    return wrapper


@spell_timer
def slow_incantation(n: int) -> str:
    """Simulate a slow spell proportional to n."""
    time.sleep(n * 0.01)
    return f"Spell of magnitude {n} complete!"


if __name__ == "__main__":
    print(slow_incantation(5))
    print(slow_incantation(10))
```

Expected output:

```
⏱  slow_incantation executed in 0.050312 seconds
Spell of magnitude 5 complete!
⏱  slow_incantation executed in 0.100418 seconds
Spell of magnitude 10 complete!
```

---

## What's Next?

- **[FuncMage project reference](../projects/funcmage.md)** — see `power_validator`, `retry_spell`, and `MageGuild` built on these foundations.
- **[Pydantic Data Modelling tutorial](pydantic-models.md)** — apply a similar "wrapping" mindset to data validation.
- **[Python Concepts Cheatsheet](../reference/concepts.md)** — quick-reference for all HOF and decorator patterns used across the curriculum.
