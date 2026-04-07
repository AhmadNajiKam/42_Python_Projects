#!/bin/env python3
import math


def str_to_float(num: str) -> float:
    sum: float = 0
    sign: int = 1
    start_idx: int = 0
    dot_idx: int
    multiplier: int = 1
    digits_dict: dict[str, int] = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9
    }
    if num and num[0] == '-':
        sign *= -1
        start_idx += 1
    dot_idx = num.find('.')
    i: int
    if dot_idx == -1:
        i = len(num) - 1
    else:
        i = dot_idx - 1

    while i >= start_idx:
        if num[i] not in digits_dict:
            raise ValueError(f"Error on parameter ’{num}’:"
                             f" could not convert string to float: ’{num}’")
        sum += multiplier * digits_dict[num[i]]
        multiplier *= 10
        i -= 1
    if dot_idx != -1:
        multiplier = 0.1
        i = dot_idx + 1
        while i < len(num):
            if num[i] not in digits_dict:
                raise ValueError(f"Error on parameter ’{num}’: "
                                 f"could not convert string to float: ’{num}’")
            sum += digits_dict[num[i]] * multiplier
            i += 1
            multiplier *= 0.1
    return sum * sign


def get_player_pos() -> tuple(float, float, float):
    while True:
        try:
            coordinates_str: str = input(
                "Enter new coordinates as floats in format ’x,y,z’: ")
            if ',' not in coordinates_str:
                raise ValueError("Invalid syntax")
            coordinates_list_str: list[str] = coordinates_str.split(',')
            coordinates_tup: tuple(float, float, float) = (
                str_to_float(coordinates_list_str[0]),
                str_to_float(coordinates_list_str[1]),
                str_to_float(coordinates_list_str[2])
            )
        except ValueError as error:
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
    coordinates_two: tuple(float, float, float) = get_player_pos()
    print("Got a second tuple:", coordinates_two)
    x2: float = coordinates_two[0]
    y2: float = coordinates_two[1]
    z2: float = coordinates_two[2]
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print("Distance between the 2 sets of coordinates:", round(distance, 4))


if __name__ == "__main__":
    main()
