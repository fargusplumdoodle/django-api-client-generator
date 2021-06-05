#!/usr/bin/python
# READ CONFIG
# RUN PARSER
# TRANSPILE
import logging

from src import DefaultSettings, logger, Settings, Validator

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    try:
        logger.info(f"Loaded settings")
        Settings.load_settings()
    except FileNotFoundError:
        logger.info(
            f'File "{DefaultSettings.SETTINGS_FILE.value}" found\n'
            f'Creating "{DefaultSettings.SETTINGS_FILE.value}"'
        )
        Settings.create_settings()
        Settings.load_settings()

    Validator.validate()
