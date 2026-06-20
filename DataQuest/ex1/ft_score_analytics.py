#!/bin/env python3
import sys


def main() -> None:
    scores_list: list[int] = []

    print("=== Player Score Analytics ===")
    for arg in sys.argv[1:]:
        try:
            num_to_add: int = int(arg)
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
