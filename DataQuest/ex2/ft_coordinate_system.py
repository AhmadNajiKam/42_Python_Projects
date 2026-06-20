#!/bin/env python3
import math


def list_size(input: list[str]) -> int:
    i: int = 0
    for item in input:
        i += 1
    return i


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coordinates_str: str = input(
                "Enter new coordinates as floats in format ’x,y,z’: ")
            if ',' not in coordinates_str:
                raise ValueError("Invalid structure")
            coordinates_list_str: list[str] = coordinates_str.split(',')
            if list_size(coordinates_list_str) != 3:
                raise Exception("Invalid input detected")
            coordinates_tup: tuple[float, float, float] = (
                float(coordinates_list_str[0]),
                float(coordinates_list_str[1]),
                float(coordinates_list_str[2])
            )
        except Exception as error:
            print(error)
        else:
            return coordinates_tup


def main() -> None:
    print("Get a first set of coordinates")
    coordinates_one: tuple[float, float, float] = get_player_pos()
    print("Got a first tuple:", coordinates_one)
    x1: float = coordinates_one[0]
    y1: float = coordinates_one[1]
    z1: float = coordinates_one[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance: float = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print("Distance to center:", round(distance, 4))

    print("\nGet a second set of coordinates")
    coordinates_two: tuple[float, float, float] = get_player_pos()
    print("Got a second tuple:", coordinates_two)
    x2: float = coordinates_two[0]
    y2: float = coordinates_two[1]
    z2: float = coordinates_two[2]
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print("Distance between the 2 sets of coordinates:", round(distance, 4))


if __name__ == "__main__":
    main()
