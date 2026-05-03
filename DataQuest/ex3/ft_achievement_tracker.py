#!/bin/env python3
import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    random_nbr: int = random.randint(1, len(achievements))
    player_list: list[str] = random.sample(achievements, k=random_nbr)
    return set(player_list)


def main() -> None:
    print("=== Achievement Tracker System ===")
    achievements: list[str] = ['Crafting Genius', 'Strategist',
                               'World Savior', 'Speed Runner',
                               'Survivor', 'Master Explorer',
                               'Treasure Hunter', 'Unstoppable',
                               'First Steps', 'Collector Supreme',
                               'Untouchable', 'Sharp Mind', 'Boss Slayer']
    player1_set: set[str] = gen_player_achievements(achievements)
    print("Player Alice:", player1_set)
    player2_set: set[str] = gen_player_achievements(achievements)
    print("Player Bob", player2_set)
    player3_set: set[str] = gen_player_achievements(achievements)
    print("Player Charlie", player3_set)
    player4_set: set[str] = gen_player_achievements(achievements)
    print("Player Dylan", player4_set)
    print("\nAll distinct achievements:", achievements)
    common_set: set[str] = player1_set.intersection(
        player2_set).intersection(player3_set).intersection(player4_set)
    print("\nCommon achievements:", common_set)

    print("\nOnly Alice has:", player1_set.difference(player2_set.union(
        player3_set).union(player4_set)))
    print("\nOnly Bob has:", player2_set.difference(player1_set.union(
        player3_set).union(player4_set)))
    print("\nOnly Charlie has:", player3_set.difference(player1_set.union(
        player2_set).union(player4_set)))
    print("\nOnly Dylan has:", player4_set.difference(player1_set.union(
        player2_set).union(player3_set)))
    print("Alice is missing:", set(achievements).difference(player1_set))
    print("Bob is missing:", set(achievements).difference(player2_set))
    print("Charlie is missing:", set(achievements).difference(player3_set))
    print("Dylan is missing:", set(achievements).difference(player4_set))


if __name__ == "__main__":
    main()
