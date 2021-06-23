import abc
import logging
from typing import Optional


class ParserError(Exception):
    PARSER_DOES_NOT_EXIST = "Parser {parser} does not exist"


class Parser(abc.ABC):
    name: str

    def __init__(self, target_dir: str, settings: Optional[dict]):
        self.target_dir = target_dir
        self.settings = settings
        self.logger = logging.getLogger(self.name)

        self.validate()

    def validate(self):
        if self.name is None:
            raise NotImplementedError("Name must be set on parser")

    def parse(self):
        # TODO: type
        self.logger.info(f"Parsing {self.target_dir}")
        collection = self._run()
        self.logger.info(f"Complete")
        return collection

    @abc.abstractmethod
    def _run(self):
        """
        Method that creates a collection from project files
        """
        pass
