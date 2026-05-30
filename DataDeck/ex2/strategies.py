from abc import ABC, abstractmethod
from ex0 import Creature
from typing import TypeGuard
from ex1 import Healer, Transformer


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack") and hasattr(creature, "describe")

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise Exception(f"Invalid Creature ’{creature.name}’"
                            " for this normal strategy")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> TypeGuard[Transformer]:
        return isinstance(creature, Transformer)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise Exception(f"Invalid Creature ’{creature.name}’"
                            " for this agggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> TypeGuard[Healer]:
        return isinstance(creature, Healer)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(f"Invalid Creature ’{creature.name}’"
                            " for this defensive strategy")
