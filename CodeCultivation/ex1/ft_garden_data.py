#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data(plant: Plant) -> None:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def main() -> None:
    plant_one = Plant("Rose", 25, 30)
    plant_two = Plant("SunFlower", 80, 45)
    plant_three = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    ft_garden_data(plant_one)
    ft_garden_data(plant_two)
    ft_garden_data(plant_three)


if __name__ == "__main__":
    main()
