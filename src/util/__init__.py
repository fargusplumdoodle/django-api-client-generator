from enum import Enum

from .settings import Settings
from .validator import Validator
from ..parser.parser import ParserError, Parser


class HTTPMethod(Enum):
    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    CONNECT = "CONNECT"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    PATCH = "PATCH"


def get_parser():
    for parser in Parser.__subclasses__():
        if parser.name == Settings.PARSER:

            parser_settings = (
                Settings.PARSER_SETTINGS[Settings.PARSER]
                if Settings.PARSER in Settings.PARSER_SETTINGS
                else None
            )
            return parser(
                target_dir=Settings.TARGET_DIRECTORY, settings=parser_settings
            )

    raise ParserError(ParserError.PARSER_DOES_NOT_EXIST.format(parser=Settings.PARSER))
