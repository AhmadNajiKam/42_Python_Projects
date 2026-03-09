#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

class ExtendedPlant(Plant):
    def __init__(self, name: str, height :int, age: int):
        super().__init__(name, height, age)
        self.growth = 0

    def grow(self) -> None:
        self.growth += 1

    def grow_older(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height + self.growth}cm, {self.age} days old")


def main() -> None:
    print("=== Day 1 ===")
    plant = ExtendedPlant("Rose", 25, 30)
    plant.get_info()
    i = 1
    while i < 7 :
        plant.grow()
        plant.grow_older()
        i += 1
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{plant.growth}cm")


if __name__ == "__main__" :
    main()
