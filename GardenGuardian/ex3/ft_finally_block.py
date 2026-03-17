#!/usr/bin/env python3
def water_plants(plant_list: list[str]) -> Exception:
    print("Opening watering system")
    for plant in plant_list:
        if plant is not None and plant != "":
            print(f"Watering {plant}")
        else:
            raise Exception("Cannot water None - invalid plant!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plant_lst: list[str] = ["tomato", "lettuce", "carrots"]
    try:
        water_plants(plant_lst)
    except Exception as error:
        print("Error:", error)
    finally:
        print("Closing watering system (cleanup)")

    plant_lst = ["tomato", None, "lettuce"]
    print("Watering completed successfully!\n")
    print("Testing with error...")
    try:
        water_plants(plant_lst)
    except Exception as error:
        print("Error:", error)
    finally:
        print("Closing watering system (cleanup)")
    print()
    print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
