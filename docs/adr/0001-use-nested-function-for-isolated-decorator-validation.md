# ADR 0001: Use Nested Function for Isolated Decorator Validation

## Status

Accepted

## Context

In the `MageGuild` class, the `cast_spell` method needs to apply runtime parameter validation using the `@power_validator` decorator.

Python decorators are typically applied at the function definition level. If we apply the decorator directly to the public `cast_spell` method, the signature expected by the decorator might clash with the public instance method signature (which automatically passes `self` as the first argument).

Furthermore, we only want the validation logic to apply strictly to the core execution of casting the spell, keeping it cleanly isolated from any potential preprocessing or postprocessing logic inside `cast_spell`.

## Decision

We decided to encapsulate the core spell execution logic inside a nested, inner function named `_cast` directly within the `cast_spell` method, and apply the `@power_validator` decorator to this inner function.

```python
def cast_spell(self, spell_name: str, power: int) -> str:
    @power_validator(min_power=10)
    def _cast(power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"
    return str(_cast(power, spell_name))

```

The leading underscore in `_cast` explicitly marks it as a private helper implementation detail that is completely hidden from the rest of the class.

## Consequences

### Positive

* **Signature Alignment:** Avoids passing `self` into the `@power_validator` logic, ensuring the decorator only interacts with the raw validation parameters (`power`).
* **Encapsulation:** The validation routine is localized entirely within `cast_spell`. No other methods in `MageGuild` can accidentally call or interfere with `_cast`.
* **Readability:** Keeping the execution close to the validation logic makes it immediately clear how the parameters are being evaluated.

### Negative

* **Performance Overhead:** The `_cast` function is redefined dynamically every single time `cast_spell` is called. For this codebase's scale, the overhead of creating a function object is negligible, but it is worth noting for tight loops.
* **Testing:** The inner `_cast` function cannot be unit-tested in isolation; it can only be tested implicitly by calling `cast_spell`.

