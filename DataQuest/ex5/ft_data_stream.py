#!/bin/env python3
import random
import typing


def consume_event(events_list: list[tuple[str, str]]) -> typing.Generator[
        tuple[str, str], None, None]:
    while len(events_list) != 0:
        choice: tuple[str, str]
        choice = random.choice(events_list)
        events_list.remove(choice)
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
        events_list.append(row)
    generator = consume_event(events_list)
    for element in range(len(events_list)):
        row = next(generator)
        print(f"Got event from list: {row}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
