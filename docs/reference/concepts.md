# Python Concepts Cheatsheet

Quick-reference for all patterns used across the 42 Python curriculum.

---

## Higher-Order Functions

```python
# map — transform every element
list(map(lambda x: x ** 2, [1, 2, 3]))        # [1, 4, 9]

# filter — keep elements matching predicate
list(filter(lambda x: x % 2 == 0, [1,2,3,4])) # [2, 4]

# reduce — fold left
from functools import reduce
reduce(lambda acc, x: acc + x, [1,2,3,4])      # 10

# sorted with key
sorted(["banana", "fig", "apple"], key=len)    # ['fig', 'apple', 'banana']
```

---

## Decorators

```python
import functools

def my_decorator(func):
    @functools.wraps(func)          # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

@my_decorator
def my_function(): ...
```

**Decorator with arguments** (factory pattern):

```python
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello(): print("hi")
```

---

## Generators

```python
# Generator function
def count_up(start, stop):
    while start <= stop:
        yield start
        start += 1

# Generator expression (lazy)
squares = (x ** 2 for x in range(10))

# Consume
next(squares)     # 0
list(squares)     # [1, 4, 9, ... 81]  (0 already consumed)

# yield from — delegate to sub-generator
def chain(*iterables):
    for it in iterables:
        yield from it
```

---

## Pydantic v2

```python
from pydantic import BaseModel, field_validator
from typing import Annotated
from pydantic import Field

class Item(BaseModel):
    name: str
    price: Annotated[float, Field(gt=0)]          # greater-than constraint
    tags: list[str] = []

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("name cannot be blank")
        return v.strip()

item = Item(name=" Widget ", price=9.99)
print(item.name)              # "Widget"
print(item.model_dump())      # {'name': 'Widget', 'price': 9.99, 'tags': []}
print(item.model_dump_json()) # '{"name":"Widget","price":9.99,"tags":[]}'
```

**Settings from `.env`:**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    debug: bool = False
    model_config = {"env_file": ".env"}

s = Settings()
```

---

## Typing

```python
from typing import Protocol, TypeVar, Callable

# Protocol — structural subtyping (duck typing with types)
class Drawable(Protocol):
    def draw(self) -> None: ...

def render(item: Drawable) -> None:
    item.draw()

# TypeVar — generic functions
T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

# Callable — type-hint functions
def apply(f: Callable[[int], int], x: int) -> int:
    return f(x)
```

---

## Context Managers

```python
# Using with (file)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Custom context manager with contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire()
    try:
        yield resource
    finally:
        release(resource)
```

---

## Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# Dict comprehension
word_lengths = {word: len(word) for word in ["hello", "world"]}

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "hi"]}

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
```

---

## `functools` Quick Reference

| Function | Use |
|---|---|
| `functools.wraps(func)` | Copy metadata to wrapper |
| `functools.reduce(f, iterable)` | Fold left with binary function |
| `functools.partial(f, *args)` | Pre-fill arguments |
| `functools.lru_cache(maxsize=128)` | Memoise return values |
| `functools.cache` | Unbounded memoisation (Python 3.9+) |
