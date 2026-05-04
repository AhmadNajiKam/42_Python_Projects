#!/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    data: str = ""
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
        print(f"Error opening file ’{filename}’:", error)
    except PermissionError as error:
        print(f"Error opening file ’{filename}’:", error)
    except IsADirectoryError as error:
        print(f"Error opening file ’{filename}’:", error)
    except OSError as error:
        print("A system error occurred:", error)
    finally:
        if file is not None:
            file.close()
            print(f"File ’{filename}’ closed.")
        else:
            print(f"File ’{filename}’ was never opened.")

    print("Transform data:")
    try:
        new_file: typing.Optional[typing.TextIO] = None
        data = data.replace("\n", "#\n")
        print("---\n")
        print(data)
        print("---")
        new_file_name: str = input("Enter new file name (or empty):")
        if not new_file_name:
            print("Not saving data.")
            return
        new_file = open(new_file_name, "w")
        new_file.write(data)
        print(f"Saving data to ’{new_file_name}’")
        print(f"Data saved in file ’{new_file_name}’.")
    except OSError as error:
        print("A system error occurred:", error)
    finally:
        if new_file:
            new_file.close()


if __name__ == "__main__":
    main()
