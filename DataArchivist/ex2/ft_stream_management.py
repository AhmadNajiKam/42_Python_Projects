#!/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    data: str = ""
    fail: int = 0
    try:
        filename: str = sys.argv[1]
        print(f"Accessing file ’{filename}’")
        file: typing.Optional[typing.TextIO] = None
        file = open(filename, "r")
        data = file.read()
        print("---\n")
        print(data)
        print("---")
    except FileNotFoundError as error:
        sys.stderr.write(f"[STDERR] Error opening file ’{
                         filename}’: {error}\n")
    except PermissionError as error:
        sys.stderr.write(f"[STDERR] Error opening file ’{
                         filename}’: {error}\n")
    except IsADirectoryError as error:
        sys.stderr.write(f"[STDERR] Error opening file ’{
                         filename}’: {error}\n")
    except OSError as error:
        sys.stderr.write(f"[STDERR] A system error occurred: {error}")
    finally:
        if file is not None:
            file.close()
            print(f"File ’{filename}’ closed.")
        else:
            print(f"File ’{filename}’ was never opened.")
            fail = 1

    if fail:
        return
    print("Transform data:")
    try:
        new_file: typing.Optional[typing.TextIO] = None
        data = data.replace("\n", "#\n")
        print("---\n")
        print(data)
        print("---")
        sys.stdout.write("Enter new file name (or empty):")
        sys.stdout.flush()
        new_file_name: str = sys.stdin.readline().removesuffix("\n")
        if not new_file_name:
            print("Not saving data.")
            return
        new_file = open(new_file_name, "w")
        new_file.write(data)
        print(f"Saving data to ’{new_file_name}’")
        print(f"Data saved in file ’{new_file_name}’.")
    except FileNotFoundError as error:
        sys.stderr.write(f"[STDERR] Error opening file ’{
                         filename}’: {error}\n")
    except PermissionError as error:
        sys.stderr.write(f"[STDERR] Error opening file ’{
                         filename}’: {error}\n")
    except IsADirectoryError as error:
        sys.stderr.write(f"[STDERR] Error opening file ’{
                         filename}’: {error}\n")
    except OSError as error:
        sys.stderr.write(f"[STDERR] A system error occurred: {error}\n")
    finally:
        if new_file is not None:
            new_file.close()
            print(f"File ’{new_file_name}’ closed.")


if __name__ == "__main__":
    main()
