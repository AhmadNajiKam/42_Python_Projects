#!/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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
                total} items processed, remaining {
                len(proc[0].data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        out_list: list[tuple[int, str]] = []
        for proc in self.__processors:
            out_list.clear()
            for item in range(nb):
                if len(proc[0].data) == 0:
                    break
                tup: tuple[int, str] = proc[0].output()
                out_list.append(tup)
            plugin.process_output(out_list)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        size: int = len(data)
        if size == 0:
            print("CSV Output: ")
            return

        print("CSV Output:")
        for i, item in enumerate(data):
            if i < size - 1:
                print(f"{str(item[1])}", end=", ")
            else:
                print(f"{str(item[1])}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        size: int = len(data)
        if size == 0:
            print("JSON Output: ")
            return

        print("JSON Output:")
        for i, item in enumerate(data):
            if i == 0:
                print("{", end="")
            if i < size - 1:
                print(f"\"item_{item[0]}\" : \"{item[1]}\"", end=", ")
            else:
                print(f"\"item_{item[0]}\" : \"{item[1]}\"")
            if i == size - 1:
                print("}")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    ds: DataStream = DataStream()
    np: NumericProcessor = NumericProcessor()
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()
    ds.print_processors_stats()
    print("Registering Processors")
    data_batch: list[Any] = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING",
          "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO",
         "log_message": "User wil is connected"}
         ], 42, ["Hi", "five"]]

    print("Send first batch of data on stream:")
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)
    ds.process_stream(data_batch)
    ds.print_processors_stats()
    csvPlugin = CSVExportPlugin()
    jsonPlugin = JSONExportPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, csvPlugin)
    print()
    ds.print_processors_stats()
    print("Send another batch of data:")
    data_batch = [21, ["I love AI", "LLMs are wonderful", "Stay healthy"],
                  [{"log_level": "ERROR", "log_message": "500 server crash"},
                   {"log_level": "NOTICE",
                    "log_message": "Certificate expires in 10 days"}],
                  [32, 42, 64, 84, 128, 168],
                  "World hello"]
    ds.process_stream(data_batch)
    ds.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, jsonPlugin)
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
