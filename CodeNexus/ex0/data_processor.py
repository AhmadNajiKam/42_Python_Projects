#!/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.counter: int = 0
        self.data: list[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.data) == 0:
            return (0, "")
        tup: tuple[int, str] = (self.counter, self.data[0])
        self.counter += 1
        self.data.pop(0)
        return tup


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        def check_num(data: str) -> bool:
            try:
                float(data)
                return True
            except ValueError:
                return False

        if isinstance(data, str):
            return check_num(data)

        if isinstance(data, list):
            if not data:
                return True
            return all(isinstance(x, (int, float)) or (
                isinstance(x, str) and check_num(x)) for x in data)
        return False

    def ingest(self, data: int | float | list[float | int]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric value")
        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
        else:
            self.data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def check_num(data: str) -> bool:
            try:
                float(data)
                return True
            except ValueError:
                return False

        if isinstance(data, str):
            return not check_num(data)
        if isinstance(data, list):
            if not data:
                return True
            return all((isinstance(item, str) and not check_num(item)
                        ) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text value")
        if isinstance(data, list):
            for item in data:
                self.data.append(item)
        else:
            self.data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def check_right_dict(item: dict[str, str]) -> bool:
            if not isinstance(item, dict):
                return False
            if ("log_message" in item
                    and "log_level" in item and
                    isinstance(item["log_message"], str)
                    and isinstance(item["log_level"], str)):
                return True
            return False

        if isinstance(data, list):
            return all(check_right_dict(item) for item in data)

        return check_right_dict(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper dictionary value")
        if isinstance(data, list):
            for item in data:
                self.data.append(f"{item['log_level']}: {item['log_message']}")
        else:
            self.data.append(f"{data['log_level']}: {data['log_message']}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    np: NumericProcessor = NumericProcessor()
    print("Trying to validate input ’42’:", np.validate(42))
    print("Trying to validate input ’Hello’:", np.validate("Hello"))
    try:
        print("Test invalid ingestion of string ’foo’"
              "without prior validation:")
        print(np.ingest("foo"))
    except Exception as error:
        print("Got exception:", error)
    print("Processing data:", [1, 2, 3, 4, 5])
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    tup: tuple[int, str] = np.output()
    print(f"Numeric value {tup[0]}: {tup[1]}")
    tup = np.output()
    print(f"Numeric value {tup[0]}: {tup[1]}")
    tup = np.output()
    print(f"Numeric value {tup[0]}: {tup[1]}")
    print()

    tp: TextProcessor = TextProcessor()
    print("Testing Text Processor...")
    print("Trying to validate input ’42’:", tp.validate(42))
    print("Trying to validate input ’Hello’:", tp.validate("Hello"))
    try:
        print("Test invalid ingestion of string ’42’ "
              "without prior validation:")
        print(tp.ingest("42"))
    except Exception as error:
        print("Got exception:", error)
    print("Processing data:", ["Hello", "Nexus", "World"])
    tp.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    tup = tp.output()
    print(f"Numeric value {tup[0]}: {tup[1]}")
    print()

    lp: LogProcessor = LogProcessor()
    print("Testing Log Processor...")
    print("Trying to validate input ’Hello’:", lp.validate("Hello"))

    test_dict: dict[str, str] = dict(
        {"log_level": "NOTICE", "log_message": "Connection to server"}
    )
    print(f"Trying to validate input ’{test_dict}’:", lp.validate(test_dict))
    try:
        print("Test invalid ingestion of string ’42’ "
              "without prior validation:")
        print(lp.ingest("42"))
    except Exception as error:
        print("Got exception:", error)
    test_dict_lst: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message":
         "Connection to server"}, {"log_level": "ERROR", "log_message":
                                   "Unauthorized access!!"}]
    print("Processing data:", test_dict_lst)
    lp.ingest(test_dict_lst)
    print("Extracting 2 values...")
    tup = lp.output()
    print(f"Numeric value {tup[0]}: {tup[1]}")
    tup = lp.output()
    print(f"Numeric value {tup[0]}: {tup[1]}")
    print()


if __name__ == "__main__":
    main()
