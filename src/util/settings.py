import sys
import logging

from enum import Enum

import yaml
from yaml import Dumper


logger = logging.getLogger(__name__)


class DefaultSettings(Enum):
    PARSER = "django"
    SETTINGS_FILE = "./settings.yml"
    TARGET_DIRECTORY = ""
    PARSER_SETTINGS = {
        "django": {"project_app": "budget", "settings_module": "settings"}
    }


class Settings:
    TARGET_DIRECTORY = sys.argv[1]
    SETTINGS_FILE = "./settings.yml"
    PARSER = "django"
    PARSER_SETTINGS = {}

    @classmethod
    def load_settings(
        cls, settings_location: str = DefaultSettings.SETTINGS_FILE.value
    ) -> None:
        """
        :raises yaml.YAMLError
        """
        with open(settings_location, "r") as f:
            data = f.read()

        yml = yaml.safe_load(data)
        for item in yml:
            setattr(cls, item, yml[item])

    @staticmethod
    def create_settings(file: str = DefaultSettings.SETTINGS_FILE.value) -> None:
        with open(file, "w") as f:
            settings_list = {item.name: item.value for item in DefaultSettings}
            f.write(yaml.dump(settings_list, Dumper=Dumper))
