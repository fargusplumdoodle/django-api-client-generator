import abc
import os
from typing import Type

from src import Settings


class ParserError(Exception):
    PARSER_DOES_NOT_EXIST = f"Parser {Settings.PARSER} does not exist"


class Parser(abc.ABC):
    ParserError = ParserError
    name: str

    def __init__(self, target_dir: str):
        self.target_dir: str = target_dir
        self.validate()

    def validate(self):
        if not os.path.exists(self.target_dir):
            self.ParserError(
                self.ParserError.TARGET_DIR_DOESNT_EXIST.format(
                    target_dir=Settings.TARGET_DIRECTORY
                )
            )

    @classmethod
    def get_parser(cls):
        for parser in cls.__subclasses__():
            if parser.name == Settings.PARSER:
                return parser(Settings.TARGET_DIRECTORY)
