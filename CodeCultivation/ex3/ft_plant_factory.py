#!/usr/bin/env python3

class Plant:
    count: int = 0

    def __init__(self, name: str = "Plant",
                 height: int = 0, age: int = 0) -> None:
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")
        Plant.count += 1


def main() -> None:
    print("=== Plant Factory Output ===")
    plant_one = Plant("Rose", 25, 30)
    plant_two = Plant("Oak", 200, 365)
    plant_three = Plant("Cactus", 5, 90)
    plant_four = Plant("Sunflower", 80, 45)
    plant_five = Plant("Fern", 15, 120)
    del plant_one, plant_two, plant_three, plant_four, plant_five
    print(f"\nTotal plants created: {Plant.count}")


if __name__ == "__main__":
    main()
