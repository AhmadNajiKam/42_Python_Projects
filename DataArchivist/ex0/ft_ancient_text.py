#!/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        filename: str = sys.argv[1]
        print(f"Accessing file ’{filename}’")
        file: typing.Optional[typing.TextIO] = None
        file = open(filename, "r")
        data: str = file.read()
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


if __name__ == "__main__":
    main()
