#!/usr/bin/env python3

def check_temperature(temp_str: str) -> None | int:
    try:
        print("Testing temperature: ")
        temp_int: int = int(temp_str)
        if temp_int > 40:
            raise Exception(
                f"Error: {temp_str}°C is too hot for plants (max 40°C)"
            )
        elif temp_int < 0:
            raise Exception(
                f"Error: {temp_str}°C is too cold for plants (min 0°C)"
            )
    except ValueError:
        print(f"Error: ’{temp_str}’ is not a valid number")
    except Exception as error:
        print(error)
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn’t crash!")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()
