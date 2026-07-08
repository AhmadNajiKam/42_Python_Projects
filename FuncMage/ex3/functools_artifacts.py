#!/bin/env python3
from typing import TypedDict, Any, Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


class PartialEnchanter(TypedDict):
    version_one: Callable[[str], str]
    version_two: Callable[[str], str]
    version_three: Callable[[str], str]


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    else:
        raise ValueError("Operation is unknown")


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> PartialEnchanter:
    if not callable(base_enchantment):
        raise ValueError(f"base_enchantment isn't callable it's {
            type(base_enchantment)}")
    return {
        "version_one": partial(base_enchantment, 50, "Flaming"),
        "version_two": partial(base_enchantment, 50, "Freezing"),
        "version_three": partial(base_enchantment, 50, "Poisoning")
    }


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def process_spell(spell: Any) -> str:
        return f"Unknown spell form: Cannot cast {type(spell)}"

    @process_spell.register
    def _(spell: int) -> str:
        return f"Cast Damage Spell: Dealt {spell} magical damage!"

    @process_spell.register
    def _(spell: str) -> str:
        return f"Cast Enchantment: Applied '{spell}' buff to target!"

    @process_spell.register(list)
    def _(spell: list[Any]) -> str:
        return f"Cast Multi-Cast: Chained {len(spell)} spells together!"
    return process_spell


def main() -> None:
    print("Testing spell reducer...")
    test_spells: list[int] = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(test_spells, 'add')}")
    print(f"Product: {spell_reducer(test_spells, 'multiply')}")
    print(f"Max: {spell_reducer(test_spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher: Callable[[Any], str] = spell_dispatcher()

    print(f"Damage spell: {dispatcher(42)}")

    print(f"Enchantment: {dispatcher('fireball')}")

    print(f"Multi-cast: {dispatcher([1, 2, 3])}")

    print(f"Unknown spell type: {dispatcher(3.14)}")


if __name__ == "__main__":
    main()
