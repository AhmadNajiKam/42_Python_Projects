#!/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    initial_list: list[str] = ["Alice", "bob", "Charlie", "dylan",
                               "Emma", "Gregory", "john", "kevin", "Liam"]
    second_list: list[str] = [e.capitalize() for e in initial_list]
    score_dict: dict[str, int] = {
        e: random.randrange(1000) for e in second_list}
    print("Initial list of players:", initial_list)
    print("New list of capitalized names only:", second_list)
    print("Score dict:", score_dict)
    total: int = 0
    total = sum(score_dict[k] for k in score_dict)
    avg: float = round(total / len(score_dict), 1)
    print("Score average is", avg)
    second_dict: dict[str, int] = {e: score for e in initial_list if (
        score := random.randrange(1000)) > avg}
    print("High scores:", second_dict)


if __name__ == "__main__":
    main()
