import logging
import os
import sys
from enum import Enum

import yaml
from yaml import Dumper


logger = logging.getLogger(__name__)


class DefaultSettings(Enum):
    PARSER = "django"
    SETTINGS_FILE = "./settings.yml"
    TARGET_DIRECTORY = ""


class Settings:
    TARGET_DIRECTORY = sys.argv[1]
    PARSER = "django"

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


class Validator:
    class Error(Exception):
        TARGET_DIR_DOESNT_EXIST = (
            f"Target directory '{Settings.TARGET_DIRECTORY}' does not exist"
        )

    @classmethod
    def validate(cls):
        for func_name in cls.__dict__:
            if func_name.startswith("check_"):
                try:
                    getattr(Validator, func_name)()
                except Validator.Error as e:
                    logger.error(str(e))

    @staticmethod
    def check_target_directory():
        target = Settings.TARGET_DIRECTORY
        if not os.path.exists(target):
            raise Validator.Error(
                Validator.Error.TARGET_DIR_DOESNT_EXIST.format(target_dir=target)
            )
