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
                self.data.append(str(item))
        else:
            self.data.append(str(data))


class DataStream:
    def __init__(self) -> None:
        self.__processors: list[tuple[DataProcessor, str]] = []

    def register_processor(self, proc: DataProcessor) -> None:
        name: str = ""
        if isinstance(proc, DataProcessor):
            if isinstance(proc, NumericProcessor):
                name = "Numeric Processor"
            elif isinstance(proc, TextProcessor):
                name = "Text Processor"
            elif isinstance(proc, LogProcessor):
                name = "Log Processor"
        self.__processors.append((proc, name))

    def process_stream(self, stream: list[Any]) -> None:
        got_validated: bool = False
        for item in stream:
            got_validated = False
            for proc in self.__processors:
                if proc[0].validate(item):
                    proc[0].ingest(item)
                    got_validated = True
            if not got_validated:
                print("DataStream error - Can't process "
                      f"element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.__processors) == 0:
            print("No processor found, no data")
            return
        for proc in self.__processors:
            total: int = proc[0].counter + len(proc[0].data)
            print(f"{proc[1]}: total {
                total} items processed , remaining {
                len(proc[0].data)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream: list[Any]
    ds: DataStream = DataStream()
    np: NumericProcessor = NumericProcessor()
    ds.register_processor(np)
    print("\nRegistering Numeric Processor\n")
    data_stream = ["Hello world", [3.14, -1, 2.71],
                   [{"log_level": "WARNING",
                     "log_message": "Telnet access!Use ssh instead"},
                    {"log_level": "INFO",
                     "log_message": "User wil is connected"}
                    ], 42, ["Hi", "five"]]
    print("Send first batch of data on stream:", data_stream)
    ds.process_stream(data_stream)
    ds.print_processors_stats()
    print()

    print("Registering other data processors")
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()
    print("Send the same batch again")
    ds.register_processor(tp)
    ds.register_processor(lp)
    ds.process_stream(data_stream)
    ds.print_processors_stats()
    print()
    print("Consume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    np.output()
    np.output()
    np.output()
    tp.output()
    tp.output()
    lp.output()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
