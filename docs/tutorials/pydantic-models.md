# Tutorial: Pydantic Data Modelling

**Goal:** Model alien contact logs (as in **CosmicData**) using Pydantic v2. You'll learn `BaseModel`, field validators, nested models, environment config, and `model_dump()`.

**Time:** ~30 minutes  
**Prerequisites:** Basic Python classes. No prior Pydantic knowledge needed.

---

## 1. Why Pydantic?

Python dicts and dataclasses give you no runtime validation:

```python
# This silently accepts garbage data
crew = {"name": "Ahmad", "age": "not a number", "mission": None}
```

Pydantic validates *at instantiation time* and gives you clear error messages:

```python
from pydantic import BaseModel

class CrewMember(BaseModel):
    name: str
    age: int

member = CrewMember(name="Ahmad", age="not a number")
# ValidationError: 1 validation error for CrewMember
# age: Input should be a valid integer [...]
```

---

## 2. Your First Model

```python
from pydantic import BaseModel
from datetime import datetime

class ContactLog(BaseModel):
    signal_id: str
    received_at: datetime
    frequency_mhz: float
    decoded_message: str | None = None  # optional field with default
```

Instantiate it:

```python
log = ContactLog(
    signal_id="SIG-001",
    received_at="2025-03-14T09:26:53",  # Pydantic parses ISO strings automatically
    frequency_mhz=1420.405,
)

print(log.signal_id)        # SIG-001
print(log.received_at)      # 2025-03-14 09:26:53
print(log.decoded_message)  # None
```

!!! info "Automatic coercion"
    Pydantic v2 is *strict by default for types but lenient for common conversions*. 
    A string `"2025-03-14T09:26:53"` is automatically coerced to `datetime`. 
    A string `"not a number"` for a `float` field is **not** — that raises a `ValidationError`.

---

## 3. Field Validators

Use `@field_validator` to enforce domain rules:

```python
from pydantic import BaseModel, field_validator

class ContactLog(BaseModel):
    signal_id: str
    frequency_mhz: float

    @field_validator("signal_id")
    @classmethod
    def signal_id_must_be_prefixed(cls, v: str) -> str:
        if not v.startswith("SIG-"):
            raise ValueError("signal_id must start with 'SIG-'")
        return v.upper()  # normalise to uppercase

    @field_validator("frequency_mhz")
    @classmethod
    def frequency_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("frequency_mhz must be positive")
        return v
```

Test the validation:

```python
ContactLog(signal_id="INVALID", frequency_mhz=1420.405)
# ValidationError: signal_id must start with 'SIG-'

ContactLog(signal_id="SIG-001", frequency_mhz=-5.0)
# ValidationError: frequency_mhz must be positive

log = ContactLog(signal_id="sig-001", frequency_mhz=1420.405)
print(log.signal_id)  # SIG-001  ← normalised
```

---

## 4. Nested Models

Models can contain other models:

```python
from pydantic import BaseModel
from datetime import datetime

class Location(BaseModel):
    constellation: str
    light_years_away: float

class ContactLog(BaseModel):
    signal_id: str
    received_at: datetime
    frequency_mhz: float
    origin: Location                  # nested model
    decoded_message: str | None = None

log = ContactLog(
    signal_id="SIG-042",
    received_at="2025-06-01T00:00:00",
    frequency_mhz=1420.405,
    origin={"constellation": "Orion", "light_years_away": 1344.0},  # dict works too
)

print(log.origin.constellation)  # Orion
```

---

## 5. Serialisation with `model_dump()`

Convert back to a plain dict for JSON serialisation, database writes, etc.:

```python
data = log.model_dump()
# {
#   'signal_id': 'SIG-042',
#   'received_at': datetime(2025, 6, 1, 0, 0),
#   'frequency_mhz': 1420.405,
#   'origin': {'constellation': 'Orion', 'light_years_away': 1344.0},
#   'decoded_message': None
# }

# JSON-safe (datetime → ISO string):
import json
json_str = log.model_dump_json()
```

---

## 6. Environment Config with `BaseSettings`

In **CosmicData** (and the `python-dotenv` exercises), config is loaded from `.env`:

```python
# .env
DATABASE_URL=postgresql://localhost/cosmic
MAX_SIGNALS=1000
DEBUG=true
```

```python
from pydantic_settings import BaseSettings  # pip install pydantic-settings

class Settings(BaseSettings):
    database_url: str
    max_signals: int = 500
    debug: bool = False

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

settings = Settings()
print(settings.database_url)  # postgresql://localhost/cosmic
print(settings.debug)         # True  ← coerced from string "true"
```

!!! tip "Pydantic Settings is separate"
    In Pydantic v2, `BaseSettings` moved to the `pydantic-settings` package. 
    Install it with `pip install pydantic-settings`, not just `pydantic`.

---

## 7. Full CosmicData Example

```python
from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, field_validator


class AlienCrewMember(BaseModel):
    name: str
    role: str
    health: int = 100

    @field_validator("health")
    @classmethod
    def health_in_range(cls, v: int) -> int:
        if not (0 <= v <= 100):
            raise ValueError("health must be between 0 and 100")
        return v


class SpaceStation(BaseModel):
    station_id: str
    crew: list[AlienCrewMember]
    operational: bool = True

    @property
    def crew_count(self) -> int:
        return len(self.crew)


station = SpaceStation(
    station_id="DEEP-SPACE-9",
    crew=[
        {"name": "Zorg", "role": "Commander", "health": 95},
        {"name": "Glrix", "role": "Engineer", "health": 78},
    ],
)

print(station.crew_count)       # 2
print(station.crew[0].name)     # Zorg
print(station.model_dump_json(indent=2))
```

---

## What's Next?

- **[CosmicData project reference](../projects/cosmicdata.md)** — the full model hierarchy used in the submission.
- **[How to Run Tests Locally](../how-to/run-tests.md)** — validate your models against the exercise specs.
- **[Python Concepts Cheatsheet](../reference/concepts.md)** — Pydantic v2 field types quick-reference.
