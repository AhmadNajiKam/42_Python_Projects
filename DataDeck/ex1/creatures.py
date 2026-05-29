from .capabilities import HealCapability, TransformCapability
from ex0 import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.state: str = "Normal"

    def attack(self) -> str:
        if self.state == "Normal":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.state = "sharper"
        return f"{self.name} shifts into a {self.state} form!"

    def revert(self) -> str:
        self.state = "Normal"
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal")
        self.state: str = "Normal"

    def attack(self) -> str:
        if self.state == "Normal":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.state = "dragonic battle"
        return f"{self.name} morphs into a {self.state} form!"

    def revert(self) -> str:
        self.state = "Normal"
        return f"{self.name} stabilizes its form."
