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


def main() -> None:
    scores_list: list[int] = []

    print("=== Player Score Analytics ===")
    for arg in sys.argv[1:]:
        try:
            num_to_add: int = atoi(arg)
            scores_list[len(scores_list):] += [num_to_add]
        except ValueError:
            print(f"Invalid parameter: {arg}")
    if len(scores_list) == 0:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return
    print("Scores processed:", scores_list)
    print("Total players:", len(scores_list))
    print("Total score:", sum(scores_list))
    print("Average score:", sum(scores_list) / len(scores_list))
    print("High score:", max(scores_list))
    print("Low score:", min(scores_list))
    print("Score range:", max(scores_list) - min(scores_list))


if __name__ == "__main__":
    main()
