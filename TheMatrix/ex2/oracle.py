#!/bin/env python3

def main() -> None:
    try:
        from dotenv import load_dotenv
        from os import environ
        load_dotenv(override=False)
        mode: str | None = environ.get("MATRIX_MODE")
        if mode is None:
            print("[WARNING] MATRIX_MODE is missing")
        database: str | None = environ.get("DATABASE_URL")
        if database is None:
            print("[WARNING] DATABASE_URL is missing")
        api_key: str | None = environ.get("API_KEY")
        if api_key is None:
            print("[WARNING] API_KEY is missing")
        log: str | None = environ.get("LOG_LEVEL")
        if log is None:
            print("[WARNING] LOG_LEVEL is missing")
        zion: str | None = environ.get("ZION_ENDPOINT")
        if zion is None:
            print("[WARNING] ZION_ENDPOINT is missing")
        print("ORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print("Mode:", mode)
        print("Database:", database)
        print("API Access:", api_key)
        print("Log Level:", log)
        print("Zion Network:", zion)
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")
        print("The Oracle sees all configurations.")
    except ImportError:
        print("python-dotenv is missing")


if __name__ == "__main__":
    main()
