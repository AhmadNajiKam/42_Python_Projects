#!/bin/env python3
import sys


def atoi(num: str) -> int:
    sign: int = 1
    sum: int = 0
    start_idx: int = 0
    multiplier: int = 1
    i: int = len(num) - 1
    map_nums: dict[str, int] = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9
    }
    if num and num[0] == '-':
        sign *= -1
        start_idx += 1
    while i >= start_idx:
        if num[i] not in map_nums:
            raise ValueError("Invalid number")
        sum += multiplier * map_nums[num[i]]
        multiplier *= 10
        i -= 1
    return sum * sign


def create_dictionary(argc: int, argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for element in argv[1:]:
        components: list[str] = element.split(":")
        if len(components) != 2:
            print(f"Error - invalid parameter/s {components}")
            continue
        elif components[0] in inventory:
            print(f"Redundant item ’{components[0]}’ - discarding")
            continue
        try:
            if atoi(components[1]) < 0:
                raise Exception("Quantity is less than 0")
            inventory[components[0]] = atoi(components[1])
        except Exception as error:
            print(f"Quantity error for ’{components[0]}’: {error}")
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("Please enter some items")
        return

    inventory: dict[str, int]
    length: int = len(sys.argv)
    inventory = create_dictionary(length, sys.argv)
    dict_sum: int = sum(inventory.values())
    size: int = len(inventory.values())

    print("Got inventory:", inventory)
    print("Item list:", list(inventory.keys()))
    print(f"Total quantity of the {size} items:", dict_sum)

    try:
        for element in inventory:
            print(f"Item {element} represents {round(
                (inventory[element]/dict_sum) * 100, 1)}%")
    except ZeroDivisionError:
        print(f"Item {element} represents 0%")
    max_val: int | None
    if size != 0:
        max_val = list(inventory.values())[0]
        min_val = list(inventory.values())[0]
    else:
        max_val = 0
        min_val = 0
    max_key: str
    min_key: str

    if size != 0:
        for key in inventory:
            if inventory[key] <= min_val:
                min_val = inventory[key]
                min_key = key
            if inventory[key] >= max_val:
                max_val = inventory[key]
                max_key = key
        print(f"Item most abundant: {max_key} with quantity {max_val}")
        print(f"Item least abundant: {min_key} with quantity {min_val}")
    else:
        print(f"Item most abundant: {max_val}")
        print(f"Item least abundant: {min_val}")
    inventory["magic_item"] = 1
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
