#!/bin/env python3
from ex0 import (FlameFactory, AquaFactory,
                 CreatureFactory, Creature)


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    baseCreature: Creature = factory.create_base()
    evolvedCreature: Creature = factory.create_evolved()
    print(baseCreature.describe())
    print(baseCreature.attack())
    print(evolvedCreature.describe())
    print(evolvedCreature.attack())


def test_both_factories(factoryOne: CreatureFactory,
                        factoryTwo: CreatureFactory) -> None:
    print("Testing battle")
    baseCreatureOne: Creature = factoryOne.create_base()
    baseCreatureTwo: Creature = factoryTwo.create_base()
    print(baseCreatureOne.describe())
    print("vs.")
    print(baseCreatureTwo.describe())
    print("fight!")
    print(baseCreatureOne.attack())
    print(baseCreatureTwo.attack())


def main() -> None:
    flameFactory: CreatureFactory = FlameFactory()
    aquaFactory: CreatureFactory = AquaFactory()
    test_factory(flameFactory)
    print()
    test_factory(aquaFactory)
    print()
    test_both_factories(flameFactory, aquaFactory)


if __name__ == "__main__":
    main()
