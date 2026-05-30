#!/bin/env python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy, BattleStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    num_opponents: int = len(opponents)
    for i in range(num_opponents):
        for j in range(i + 1, num_opponents):
            print("* Battle *")
            factoryOne, strategyOne = opponents[i]
            factoryTwo, strategyTwo = opponents[j]
            creatureOne = factoryOne.create_base()
            creatureTwo = factoryTwo.create_base()
            print(creatureOne.describe())
            print("vs.")
            print(creatureTwo.describe())
            print("now fight!")
            try:
                strategyOne.act(creatureOne)
                strategyTwo.act(creatureTwo)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            finally:
                print()


def main() -> None:
    flameFactory: FlameFactory = FlameFactory()
    aquaFactory: AquaFactory = AquaFactory()
    healFactory: HealingCreatureFactory = HealingCreatureFactory()
    transformFactory: TransformCreatureFactory = TransformCreatureFactory()
    normalStrategy: NormalStrategy = NormalStrategy()
    aggressiveStrategy: AggressiveStrategy = AggressiveStrategy()
    defensiveStrategy: DefensiveStrategy = DefensiveStrategy()
    print("Tournament 0 (basic)")
    opponents_0 = [
        (flameFactory, normalStrategy),
        (healFactory, defensiveStrategy)
    ]
    battle(opponents_0)

    print("Tournament 1 (error)")
    opponents_1 = [
        (flameFactory, aggressiveStrategy),
        (healFactory, defensiveStrategy)
    ]
    battle(opponents_1)

    print("Tournament 2 (multiple)")
    opponents_2 = [
        (aquaFactory, normalStrategy),
        (healFactory, defensiveStrategy),
        (transformFactory, aggressiveStrategy)
    ]
    battle(opponents_2)


if __name__ == "__main__":
    main()
