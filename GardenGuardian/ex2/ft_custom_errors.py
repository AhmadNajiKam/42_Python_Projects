#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_garden_error() -> GardenError:
    raise GardenError("Garden have dead plants")


def test_plant_error(plant: str) -> PlantError:
    raise PlantError(f"The {plant} plant is wilting!")


def test_water_error() -> WaterError:
    raise WaterError("Not enough water in the tank!")


def test_all_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        test_plant_error("tomato")
    except PlantError as error:
        print("Caught PlantError:", error)
        print()

    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as error:
        print("Caught WaterError:", error)
        print()

    print("Testing catching all garden errors...")
    try:
        test_plant_error("tomato")
    except GardenError as error:
        print("Caught a garden error:", error)
    try:
        test_water_error()
    except GardenError as error:
        print("Caught a garden error:", error)
    print()
    print("All custom error types work correctly!")


def main() -> None:
    test_all_errors()


if __name__ == "__main__":
    main()
