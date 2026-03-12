#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def print_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {
              self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk: int, shade: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self.shade = shade

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.shade} square meters of shade")

    def print_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {
              self.age} days, {self.trunk} diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, nutrition_val: str) -> None:
        super().__init__(name, height, age)
        self.season = season
        self.nutrition_val = nutrition_val

    def print_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutrition_val}")

    def print_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {
              self.age} days, {self.season} harvest")


def main():
    print("=== Garden Plant Types ===")
    flower_one = Flower("Rose", 25, 30, "red")
    flower_two = Flower("Tulip", 15, 50, "white")
    tree_one = Tree("Oak", 500, 1825, 50, 78)
    tree_two = Tree("Sakura", 300, 600, 30, 40)
    vegie_one = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    vegie_two = Vegetable("Cucumber", 90, 110, "summer", "fibers")
    flower_one.print_info()
    flower_one.bloom()
    print()
    flower_two.print_info()
    flower_two.bloom()
    print()
    tree_one.print_info()
    tree_one.produce_shade()
    print()
    tree_two.print_info()
    tree_two.produce_shade()
    print()
    vegie_one.print_info()
    vegie_one.print_nutrition()
    print()
    vegie_two.print_info()
    vegie_two.print_nutrition()


if __name__ == "__main__":
    main()
