from collections.abc import Callable
from typing import TypedDict


class MemoryVault(TypedDict):
    store: Callable[[str, str], None]
    recall: Callable[[str], str]


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total: int = initial_power

    def accumulator(value: int) -> int:
        nonlocal total
        total += value
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    return lambda name: f"{enchantment_type} {name}"


def memory_vault() -> MemoryVault:
    memory_dict: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        memory_dict[key] = value

    def recall(key: str) -> str:
        if key in memory_dict:
            return memory_dict[key]
        else:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter_a: Callable[[], int] = mage_counter()
    counter_b: Callable[[], int] = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())
    print("\nTesting spell accumulator...")
    accumulator: Callable[[int], int] = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print("\nTesting enchantment factory...")
    flame_applier: Callable[[str], str] = enchantment_factory("Flaming")
    freeze_applier: Callable[[str], str] = enchantment_factory("Frozen")
    print(flame_applier("Sword"))
    print(freeze_applier("Shield"))
    print("\nTesting memory vault...")
    mem_funcs: MemoryVault = memory_vault()
    print("Store ’secret’ = 42")
    mem_funcs['store']("secret", "42")
    print("Recall ’secret’:", mem_funcs['recall']("secret"))
    print("Recall ’unknown’:", mem_funcs['recall']("unknown"))


if __name__ == "__main__":
    main()
