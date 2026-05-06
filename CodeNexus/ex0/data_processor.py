#!/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is list[str]:
            for item in data:
                try:
                    print(f"Trying to validate input '{item}': ", end="")
                    if not item.isdigit():
                        raise ValueError("Invalid data detected")
                except ValueError:
                    print("False")
                else:
                    print("True")

    def ingest(self, data: int | float | list[float | int]) -> None:
        pass


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: str | list[str]) -> None:
        pass


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        pass
