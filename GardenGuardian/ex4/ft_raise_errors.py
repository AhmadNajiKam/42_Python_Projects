#!/usr/bin/env python3

def check_plant_health(plant_name: str,
                       water_level: int, sunlight_hours: int) -> str:
    if plant_name is None or plant_name == "":
        raise Exception("Plant name cannot be empty!")
    if water_level > 10:
        raise Exception(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise Exception(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise Exception(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    elif sunlight_hours < 2:
        raise Exception(
            f"Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    return f"Plant ’{plant_name}’ is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        result: str = check_plant_health("tomato", 2, 5)
    except Exception as error:
        print("Error:", error)
    else:
        print(result)
    print()
    print("Testing empty plant name...")
    try:
        result: str = check_plant_health(None, 2, 5)
    except Exception as error:
        print("Error:", error)
    else:
        print(result)
    print()
    print("Testing bad water level...")
    try:
        result: str = check_plant_health("tomato", 15, 5)
    except Exception as error:
        print("Error:", error)
    else:
        print(result)
    print()
    print("Testing bad sunlight hours...")
    try:
        result: str = check_plant_health("tomato", 2, 0)
    except Exception as error:
        print("Error:", error)
    else:
        print(result)
    print()
    print("All error raising tests completed!")


def main() -> None:
    test_plant_checks()


if __name__ == "__main__":
    main()
