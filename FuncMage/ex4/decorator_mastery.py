#!/bin/env python3
from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> Any:
            if power >= min_power:
                return func(power, *args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {
                                i}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(s.isalpha() or s.isspace() for s in name)

    def cast_spell(self, spell_name: str, power:
                   int) -> str:
        @power_validator(min_power=10)
        def _cast(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return str(_cast(power, spell_name))


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(1.114)
        return "Result:  Fireball cast!"
    print(fireball())
    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def failed_func() -> None:
        raise Exception("Testing error")

    @retry_spell(max_attempts=3)
    def success_func() -> str:
        return "Waaaaaaagh spelled !"
    result: str = failed_func()
    print(result)
    result = success_func()
    print(result)
    print("\nTesting MageGuild...")
    mageGuild = MageGuild()
    print(mageGuild.validate_mage_name("Ahmad"))
    print(mageGuild.validate_mage_name("ra"))
    print(mageGuild.cast_spell("Lightning", 15))
    print(mageGuild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
