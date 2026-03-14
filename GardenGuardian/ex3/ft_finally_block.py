#!/usr/bin/env python3
def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is not None:
                print(f"Watering {plant}")
            else:
                raise Exception("Cannot water None - invalid plant!")
    except Exception as error:
        print("Error:", error)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plant_lst: list[str] = ["tomato", "lettuce", "carrots"]
    water_plants(plant_lst)
    plant_lst = ["tomato", None, "lettuce"]
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(plant_lst)
    print()
    print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
