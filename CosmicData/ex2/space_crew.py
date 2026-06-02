#!/bin/env python3
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validator(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")
        if not any(member.rank in (Rank.commander, Rank.captain
                                   ) for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if (self.duration_days > 365 and
                (len(list(filter(lambda crewMem: crewMem.years_experience >= 5,
                                 self.crew))) / len(self.crew) < 0.5)):
            raise ValueError(
                "Long missions (> 365 days) need 50%"
                " experienced crew (5+ years)")
        if not all(crew.is_active for crew in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    crew_valid = [
        CrewMember(
            member_id="C01", name="Sarah Connor", rank=Rank.commander,
            age=40, specialization="Mission Command", years_experience=15
        ),
        CrewMember(
            member_id="C02", name="John Smith", rank=Rank.lieutenant,
            age=32, specialization="Navigation", years_experience=6
        ),
        CrewMember(
            member_id="C03", name="Alice Johnson", rank=Rank.officer,
            age=26, specialization="Engineering", years_experience=2
        )
    ]

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew_valid,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions:.1f}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"- {member.name} ({member.rank.value
                                    }) - {member.specialization}")

    except ValidationError as e:
        print(f"Unexpected Validation Error: {e}")

    print("=========================================")
    print("Expected validation error:")

    crew_invalid = [
        CrewMember(
            member_id="C04", name="Bob Vance", rank=Rank.officer,
            age=45, specialization="Refrigeration", years_experience=20
        )
    ]

    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Unled Expedition",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=crew_invalid,
            budget_millions=50.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
