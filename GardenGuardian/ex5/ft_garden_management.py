#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str,
                 water_level: int, sunlight_hours: int) -> None:
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours


class GardenManager:
    def __init__(self, water_tank: int) -> None:
        self.plants: list[Plant] = []
        self.water_tank: int = water_tank

    def add_plant(self, plant: Plant) -> None:
        try:
            if plant.name:
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")
            else:
                raise PlantError("Plant name cannot be empty!")
        except PlantError as error:
            print(f"Error adding plant: {error}")

    def water_plant(self, plant_name: str) -> None:
        target_plant = None
        for plant in self.plants:
            if plant.name == plant_name:
                target_plant = plant
                break
        if target_plant is None:
            raise GardenError(f"Plant '{
                plant_name
            }' doesn't exist in the garden")
        if self.water_tank < 1:
            raise GardenError("Not enough water in tank")
        target_plant.water_level += 1
        self.water_tank -= 1
        print(f"Watering {plant_name} - success")

    def water_all_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                self.water_plant(plant.name)
        except GardenError as error:
            print(f"Caught GardenError: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str,
                           water_level: int, sunlight_hours: int) -> None:
        try:
            if not plant_name:
                raise Exception("Plant name cannot be empty!")
            if water_level > 10:
                raise Exception(
                    f"Water level {water_level} is too high (max 10)")
            elif water_level < 1:
                raise Exception(
                    f"Water level {water_level} is too low (min 1)")

            if sunlight_hours > 12:
                raise Exception(f"Sunlight hours {
                                sunlight_hours} is too high (max 12)")
            elif sunlight_hours < 2:
                raise Exception(f"Sunlight hours {
                                sunlight_hours} is too low (min 2)")

            print(f"{plant_name}: healthy (water: {
                  water_level}, sun: {sunlight_hours})")

        except Exception as error:
            print(f"Error checking {plant_name}: {error}")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    plant_one = Plant("tomato", 4, 8)
    plant_two = Plant("lettuce", 14, 5)
    plant_three = Plant("", 5, 5)

    garden_manager = GardenManager(2)
    garden_manager.add_plant(plant_one)
    garden_manager.add_plant(plant_two)
    garden_manager.add_plant(plant_three)
    print()

    print("Watering plants...")
    garden_manager.water_all_plants()
    print()

    print("Checking plant health...")
    garden_manager.check_plant_health(
        plant_one.name, plant_one.water_level, plant_one.sunlight_hours)
    garden_manager.check_plant_health(
        plant_two.name, plant_two.water_level, plant_two.sunlight_hours)
    print()

    print("Testing error recovery...")
    try:
        garden_manager.water_plant(plant_one.name)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
