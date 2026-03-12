#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, type: str) -> None:
        self.name = name
        self.height = height
        self.growth = 0
        self.type = type

    def print_info(self) -> None:
        print(f"- {self.name}: {self.height}cm", end="")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, type: str,
                 color: str, bloom: str) -> None:
        super().__init__(name, height, type)
        self.color = color
        self.bloom = bloom

    def print_info(self) -> None:
        super().print_info()
        print(f", {self.color} flowers ({self.bloom})", end="")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, type: str,
                 color: str, bloom: str, prize: int) -> None:
        super().__init__(name, height, type, color, bloom)
        self.prize = prize

    def print_info(self) -> None:
        super().print_info()
        print(f", Prize points: {self.prize}", end="")


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.counter = 0
        self.growth = 0
        self.regular = 0
        self.flowering = 0
        self.prize_flowers = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.counter += 1
        if plant.type == "regular":
            self.regular += 1
        elif plant.type == "flowering":
            self.flowering += 1
        elif plant.type == "prize_flowers":
            self.prize_flowers += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_plant(self, plant_name: str) -> None:
        for plant in self.plants:
            if plant.name == plant_name:
                plant.growth += 1
                plant.height += 1
                break
        self.growth += 1
        print(f"{plant_name} grew 1cm")

    def grow_all_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.grow_plant(plant.name)

    def print_types(self) -> None:
        print(f"{self.regular} regular, {self.flowering} flowering, {
              self.prize_flowers} prize flowers")


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        garden_manager = cls()
        for owner in owners:
            garden_manager.gardens.append(Garden(owner))
        return garden_manager

    class GardenStats:
        @staticmethod
        def print_stats(garden: Garden) -> None:
            print(f"=== {garden.owner}’s Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                plant.print_info()
                print()
            print()
            print(f"Plants added: {garden.counter}, Total growth: {
                  garden.growth}cm")
            print("Plant types:", end="")
            garden.print_types()

        @staticmethod
        def height_validation(garden: Garden) -> None:
            check: bool = True
            for plant in garden.plants:
                if plant.height < 0:
                    check = False
                    break
            print("Height validation test:", check)

        @staticmethod
        def print_scores_and_total(gardens: list[Garden]) -> None:
            output_str = "Garden scores - "
            garden_count = 0
            for _ in gardens:
                garden_count += 1
            current_index = 0
            for garden in gardens:
                current_index += 1
                total_score = 0
                for plant in garden.plants:
                    total_score += plant.height
                output_str += f"{garden.owner}: {total_score}"
                if current_index < garden_count:
                    output_str += ", "
            print(output_str)
            print(f"Total gardens managed: {garden_count}")


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice_garden = manager.gardens[0]
    tree = Plant("Oak Tree", 100, "regular")
    rose = FloweringPlant("Rose", 25, "flowering", "red", "blooming")
    sunflower = PrizeFlower("Sunflower", 50, "prize_flowers",
                            "yellow", "blooming", 10)
    alice_garden.add_plant(tree)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    print()
    alice_garden.grow_all_plants()
    print()

    stats = GardenManager.GardenStats
    stats.print_stats(alice_garden)
    stats.height_validation(alice_garden)
    stats.print_scores_and_total(manager.gardens)


if __name__ == "__main__":
    main()
