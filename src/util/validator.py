import os
import logging

from src.util import Settings


logger = logging.getLogger(__name__)


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
