#!/bin/env python3

def secure_archive(file_name: str, operation: str,
                   content: str = "") -> tuple[bool, str]:
    try:
        with open(file_name, operation) as file:
            data: str = ""
            if operation == "r":
                data = file.read()
                return (True, data)
            elif operation == "w":
                file.write(content)
                return (True, content)
    except Exception as error:
        return (False,
                f"[Errno {error.errno}] {error.strerror}: '{error.filename}'")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print("\nUsing ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("/etc/sudoers", "r"))
    print("\nUsing ’secure_archive’ to read from a regular file:")
    read_tup: tuple[bool, str] = secure_archive("ahmad.txt", "r")
    print(read_tup)
    print("\nUsing ’secure_archive’ to write previous content to a new file:")
    print(secure_archive("maen.txt",
                         "w", read_tup[1]))


if __name__ == "__main__":
    main()
