import os
import sys

from .parser import Parser, ParserError


class DjangoParserError(ParserError):
    NOT_A_DJANGO_PROJECT = "Target dir not a django project, unable to find {manage}"


class DjangoParser(Parser):
    name = "django"

    def _run(self):
        sys.path.insert(0, self.target_dir)
        i = __import__(self.settings["project_app"])
        project_settings = getattr(i, self.settings["settings_module"])
        print(project_settings.ROOT_URLCONF)

    def validate(self):
        super().validate()
        manage_py_path = os.path.join(self.target_dir, "manage.py")
        if not os.path.exists(manage_py_path):
            raise DjangoParserError(
                DjangoParserError.NOT_A_DJANGO_PROJECT.format(manage=manage_py_path)
            )
