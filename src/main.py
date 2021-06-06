#!/usr/bin/python
# READ CONFIG
# RUN PARSER
# TRANSPILE
import logging

from src.parser import Parser
from src.util import get_parser
from src.util.validator import Validator
from src.util.settings import DefaultSettings, Settings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        logger.info(f"Loaded settings")
        Settings.load_settings()
    except FileNotFoundError:
        logger.info(
            f'File "{Settings.SETTINGS_FILE}" not found\n'
            f'Creating "{Settings.SETTINGS_FILE}"'
        )
        Settings.create_settings()
        Settings.load_settings()

    Validator.validate()
    parser = get_parser()
    parser.parse()
