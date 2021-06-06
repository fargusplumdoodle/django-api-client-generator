import abc
import os
from typing import Type

from src.util import Settings


class ParserError(Exception):
    PARSER_DOES_NOT_EXIST = f"Parser {Settings.PARSER} does not exist"


class Parser(abc.ABC):
    ParserError = ParserError
    name: str

    def __init__(self, target_dir: str):
        self.target_dir: str = target_dir

    @classmethod
    def get_parser(cls):
        for parser in cls.__subclasses__():
            if parser.name == Settings.PARSER:
                return parser(Settings.TARGET_DIRECTORY)
