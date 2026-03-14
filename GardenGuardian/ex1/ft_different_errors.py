#!/usr/bin/env python3

def garden_operations() -> None:
    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
        open("missing.txt")
        plant = {"existing": "rose"}
        plant["missing_plant"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        plant = {"existing": "rose"}
        plant["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    garden_operations()

    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
