#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str = "Plant",
                 height: int = 0, age: int = 0) -> None:
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> "SecurePlant":
        return self.__height

    def get_age(self) -> "SecurePlant":
        return self.__age

    def print_info(self) -> None:
        print(f"{self.name} ({self.get_height()}cm, {self.get_age()} days)")


def main() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print()
    plant.set_height(-5)
    print()
    plant.print_info()


if __name__ == "__main__":
    main()
