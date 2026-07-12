# CosmicData

**Folder:** `CosmicData/`  
**Theme:** Pydantic v2 data validation — alien contact logs, space crew management  
**Key files:** `models.py`, `settings.py`

---

## Model Hierarchy

```
SpaceStation
├── station_id: str
├── operational: bool
└── crew: list[AlienCrewMember]
        ├── name: str
        ├── role: str
        └── health: int (0–100)

ContactLog
├── signal_id: str  (must start with "SIG-")
├── received_at: datetime
├── frequency_mhz: float (> 0)
├── origin: Location
│       ├── constellation: str
│       └── light_years_away: float
└── decoded_message: str | None
```

---

## Key Design Decisions

### `signal_id` normalisation

The validator both *validates* and *transforms* — it uppercases the ID so `"sig-001"` and `"SIG-001"` both result in `"SIG-001"`. This prevents duplicate entries from differing only in case.

```python
@field_validator("signal_id")
@classmethod
def signal_id_format(cls, v: str) -> str:
    v = v.upper()
    if not v.startswith("SIG-"):
        raise ValueError("signal_id must start with 'SIG-'")
    return v
```

### `health` range validation

Using `Annotated` + `Field` is cleaner than a validator for simple numeric constraints:

```python
from typing import Annotated
from pydantic import Field

health: Annotated[int, Field(ge=0, le=100)] = 100
```

### Environment config

Sensitive values (DB URLs, API keys) are loaded via `pydantic-settings`:

```python
from pydantic_settings import BaseSettings

class CosmicSettings(BaseSettings):
    database_url: str
    signal_batch_size: int = 100
    model_config = {"env_file": ".env"}
```

---

## Lessons Learned

- **`model_dump_json()`** — prefer over `json.dumps(model.model_dump())` because it handles `datetime` serialisation automatically.
- **Nested dict → nested model** — Pydantic v2 automatically coerces a raw dict into a nested `BaseModel` at instantiation. You don't need to instantiate `Location(...)` manually.
- **`pydantic-settings` is a separate package** — `pip install pydantic-settings` — not bundled with `pydantic` in v2.
