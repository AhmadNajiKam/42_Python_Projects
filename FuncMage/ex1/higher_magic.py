#!/bin/env python3
from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fire(target: str, power: int) -> str:
    return f"Fire hits {target} for {power} HP"


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    if not callable(spell1) or not callable(spell2):
        raise TypeError(f"Expected a callable spell, got {
                        type(spell1)} and {type(spell2)}")
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int
                    ) -> Callable[[str, int], str]:
    if not callable(base_spell):
        raise TypeError(f"Expected a callable spell, got {type(base_spell)}")
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    if not callable(condition) or not callable(spell):
        raise TypeError(f"Expected a callable spell, got {
                        type(condition)} and {type(spell)}")
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    validated_spells = tuple(s for s in spells if callable(s))
    if len(validated_spells) != len(spells):
        raise TypeError(
            "Expected all items in the sequence to be callable spells")
    return lambda target, power: [spell(target, power) for spell in spells]


def main() -> None:
    print("Testing spell combiner...")
    combined_heal_fire: Callable[[str, int], tuple[str, str]
                                 ] = spell_combiner(heal, fire)
    print(combined_heal_fire("Margit", 40)[0] +
          ", " + combined_heal_fire("Margit", 40)[1])
    amplified_fire: Callable[[str, int], str] = power_amplifier(fire, 5)
    print("\nTesting power amplifier...")
    print("Original:", fire("Morgott", 10))
    print("Amplified:", amplified_fire("Margit", 10))
    print("\nTesting conditional caster...")
    is_powerful: Callable[[str, int], bool] = lambda target, power: power <= 50
    powerful_fire: Callable[[str, int],
                            str] = conditional_caster(is_powerful, fire)

    print("Tree Sentinel:", powerful_fire("Tree Sentinel", 40))
    print("Draconic Tree Sentinel:",
          powerful_fire("Draconic Tree Sentinel", 80))
    print("\nTesting spell sequence...")
    spells_mapper: Callable[[str, int], list[str]
                            ] = spell_sequence([heal, fire])
    print("Radahn fight:", spells_mapper("Radahn", 90))


if __name__ == "__main__":
    main()
