#!/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import Healer, Transformer


def main() -> None:
    print("Testing Creature with healing capability")
    healFactory: HealingCreatureFactory = HealingCreatureFactory()
    transformFactory: TransformCreatureFactory = TransformCreatureFactory()
    print("base:")
    sproutling: Healer = healFactory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    print("evolved:")
    bloomelle: Healer = healFactory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())
    print()
    print("Testing Creature with transform capability")
    print("base:")
    shiftling: Transformer = transformFactory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())
    print("evolved:")
    morphagon: Transformer = transformFactory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


if __name__ == "__main__":
    main()
