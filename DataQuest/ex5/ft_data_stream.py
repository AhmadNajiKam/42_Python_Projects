#!/bin/env python3
import random
import typing


def consume_event(events_list: list[tuple[str, str]]) -> typing.Generator[
        tuple[str, str], None, None]:
    while events_list:
        choice: tuple[str, str]
        idx: int = random.randrange(len(events_list))
        choice = events_list[idx]
        events_list[idx:idx+1] = []
        yield choice


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    player_names: list[str] = ["Alice", "Bob", "John", "Mark", "Tony",
                               "Charlie", "Ahmad", "Maen"]
    actions: list[str] = ["run", "eat", "sleep",
                          "grab", "move", "walk", "climb"]
    while True:
        yield (random.choice(player_names), random.choice(actions))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator: typing.Generator[tuple[str, str], None, None] = gen_event()
    i: int = 0
    row: tuple[str, str]
    for element in range(1000):
        row = next(generator)
        print(f"Event {i} Player {row[0]} did action {row[1]}")
        i += 1
    print("Built list of 10 events: ", end="")
    events_list: list[tuple[str, str]] = []
    for element in range(10):
        row = next(generator)
        events_list[len(events_list):] = [row]
    generator = consume_event(events_list)
    for element in range(len(events_list)):
        row = next(generator)
        print(f"Got event from list: {row}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
