#!/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(max_length=200, default=None)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        spaceStationOne: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        print("Valid station created:")
        print("ID:", spaceStationOne.station_id)
        print("Name:", spaceStationOne.name)
        print("Crew:", spaceStationOne.crew_size)
        print(f"Power:{spaceStationOne.power_level}%")
        print(f"Oxygen:{spaceStationOne.oxygen_level}%")
        is_op: str = "Operational"
        if not spaceStationOne.is_operational:
            is_op = "Non-" + is_op
        print("Status:", is_op)
        print("\n========================================")
        print("Expected validation error:")
        invalid_station: SpaceStation = SpaceStation(
            station_id="TEST",
            name="Invalid Station",
            crew_size=30,
            power_level=90,
            oxygen_level=33,
            last_maintenance=datetime.now()
        )
        del invalid_station
    except ValidationError as error:
        """" Taking the fisrt error msg from the errors list"""
        print(error.errors()[0]['msg'])


if __name__ == "__main__":
    main()
