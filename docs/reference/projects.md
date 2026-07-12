# Project Catalogue

Complete reference for every project in the repository.

---

## All Projects

| Folder | Theme | Primary Skills | Key Files |
|---|---|---|---|
| `FuncMage` | Functional / Decorators | Lambdas, HOF, closures, decorators, `functools` | `decorator_mastery.py` |
| `CosmicData` | Data Validation | Pydantic v2, `BaseModel`, validators, nested models | `models.py`, `settings.py` |
| `DataArchivist` | File I/O | File streams, context managers, binary mode | `archivist.py` |
| `DataDeck` | Data Structures | Dicts, sets, comprehensions | `deck.py` |
| `DataQuest` | Generators | `yield`, generator expressions, `itertools` | `quest.py` |
| `TheCodex` | Typing | `Protocol`, `TypeVar`, `Annotated`, generics | `codex.py` |
| `TheMatrix` | Typing + HOF | Protocols, type aliases, `Callable` typing | `matrix.py` |
| `CodeCultivation` | OOP | Classes, inheritance, `__dunder__` methods | `cultivation.py` |
| `CodeNexus` | Modules / Imports | `__init__.py`, relative imports, packages | `nexus/` |
| `GardenGuardian` | OOP + Composition | Composition over inheritance, `ABC` | `guardian.py` |
| `GrowingCode` | OOP + Generators | Class-based iterators, `__iter__`, `__next__` | `growing.py` |

---

## Skill Coverage Matrix

| Skill | Projects |
|---|---|
| `lambda` / `map` / `filter` | FuncMage, DataQuest |
| `functools.reduce` | FuncMage |
| Decorators + `functools.wraps` | FuncMage |
| Pydantic `BaseModel` | CosmicData, GardenGuardian |
| `field_validator` | CosmicData |
| `BaseSettings` / `.env` | CosmicData |
| `yield` / generators | DataQuest, GrowingCode |
| `Protocol` / structural subtyping | TheCodex, TheMatrix |
| `TypeVar` / generics | TheCodex |
| `contextlib` / `with` statements | DataArchivist |
| `__iter__` / `__next__` | GrowingCode |
| `ABC` / abstract methods | GardenGuardian |
