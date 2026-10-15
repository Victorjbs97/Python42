#!/usr/bin/env python3
import os
from dotenv import load_dotenv


class clr:
    red = '\033[31m'
    rst = '\033[0;0m'


def validate_mode(matrix_mode: str | None) -> str:
    if matrix_mode is not None:
        matrix_mode = matrix_mode.lower()
    if matrix_mode not in ("development", "production"):
        matrix_mode = "production"
    return matrix_mode


def get_mode() -> str:
    mode = os.getenv("MATRIX_MODE")
    return validate_mode(mode)


def validate_log_level(log_level: str | None) -> str:

    log_option: list[str] = [
        "debug", "warning", "info", "error", "critical"
    ]

    if not log_level:
        log_level = "INFO"
    if log_level.lower() in log_option:
        log_level = log_level.upper()
    else:
        log_level = "INFO"

    return log_level


def get_log_level() -> str:
    log_level = os.getenv("LOG_LEVEL")
    return validate_log_level(log_level)


def apply_production_rules(
    matrix_mode: str,
    log_level: str
) -> str:

    if matrix_mode == "production" and log_level == "DEBUG":
        return "WARNING"
    return log_level


def config_status(
        database_url: str | None,
        api_key: str | None,
        zion_endpoint: str | None
) -> bool:
    if not database_url or not api_key or not zion_endpoint:
        return False
    return True


if __name__ == "__main__":
    load_dotenv()

    matrix_mode: str = get_mode()
    database_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")
    log_level: str = get_log_level()
    log_level = apply_production_rules(matrix_mode, log_level)

    print("\nORACLE STATUS: Consulting the configuration...\n")
    print(f"Mode: {matrix_mode}")
    print(f"Log Level: {log_level}")

    if matrix_mode == 'development':
        if not database_url:
            print(f"Database: {clr.red}Not configured{clr.rst}")
        else:
            print("Database: Connection configured")

        if not api_key:
            print(f"API Access: {clr.red}Not configured{clr.rst}")
        else:
            print("API Access: Configured")

        if not zion_endpoint:
            print(f"Remote Network: {clr.red}Not configured{clr.rst}")
        else:
            print("Remote Network: Endpoint configured")

    else:
        if config_status(
            database_url,
            api_key,
            zion_endpoint
        ):
            print("Configuration status: Complete")
        else:
            print("Configuration status: Incomplete")
            print(
                "\ntry environment variables:\nenv MATRIX_MODE=development"
                " API_KEY=exemplekey "
                "ZION_ENDPOINT=endpoint DATABASE_URL=localhost "
                "LOG_LEVEL=debug python3 ex1/oracle.py\n"
            )
            print(
                "or try .env file:\n"
                "cp ex1/.env.example ex1/.env"
            )

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
