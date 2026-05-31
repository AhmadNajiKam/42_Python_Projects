#!/bin/env python3
from typing import TypedDict


class Artifact(TypedDict):
    name: str
    power: int
    type: str


class Mage(TypedDict):
    name: str
    power: int
    element: str


class MageStats(TypedDict):
    max_power: int
    min_power: int
    avg_power: float


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    return list(filter(lambda item: item["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda item: "* " + item + " *", spells))


def mage_stats(mages: list[Mage]) -> MageStats:
    return {
        "max_power": max(mages, key=lambda item: item["power"])["power"],
        "min_power": min(mages, key=lambda item: item["power"])["power"],
        "avg_power": round(
            sum(map(lambda item: item["power"], mages)) / len(mages),
            2
        )
    }


def main() -> None:
    print("Testing artifact sorter...")
    artifacts: list[Artifact] = [
        {'name': 'Storm Crown', 'power': 112, 'type': 'relic'},
        {'name': 'Light Prism', 'power': 111, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 104, 'type': 'accessory'},
        {'name': 'Fire Staff', 'power': 106, 'type': 'armor'}]
    mages: list[Mage] = [
        {'name': 'Ash', 'power': 96, 'element': 'lightning'},
        {'name': 'Storm', 'power': 91, 'element': 'lightning'},
        {'name': 'Morgan', 'power': 76, 'element': 'shadow'},
        {'name': 'Rowan', 'power': 52, 'element': 'ice'},
        {'name': 'Ash', 'power': 94, 'element': 'earth'}]
    spells: list[str] = ['lightning', 'heal', 'blizzard', 'fireball']
    print(artifact_sorter(artifacts))
    print("\nTesting power filter...")
    print(power_filter(mages, 60))
    print("\nTesting spell transformer...")
    print(spell_transformer(spells))
    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
