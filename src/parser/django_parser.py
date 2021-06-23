import os
import sys
from types import ModuleType
from typing import Optional

from django.core.wsgi import get_wsgi_application
from django.urls import URLResolver

from .parser import Parser, ParserError
from ..util import print_obj


class DjangoParserError(ParserError):
    NOT_A_DJANGO_PROJECT = "Target dir not a django project, unable to find {manage}"


class DjangoParser(Parser):
    name = "django"

    def __init__(self, target_dir: str, settings: Optional[dict]):
        super().__init__(target_dir, settings)
        sys.path.insert(0, self.target_dir)

        self.project_app = __import__(self.settings["project_app"])
        self.project_settings = getattr(
            self.project_app, self.settings["settings_module"]
        )
        self._setup_django()

    def _run(self):
        root_url = __import__(self.project_settings.ROOT_URLCONF)
        url_patterns = []
        for url_resolver in root_url.urls.urlpatterns:
            print(url_resolver.pattern._route)
            url_patterns += url_resolver.url_patterns

        print("num", len(url_patterns))
        print(url_patterns)

    def _setup_django(self):
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE",
            f'{self.settings["project_app"]}.{self.settings["settings_module"]}',
        )
        del self.project_settings.DATABASES
        # Forcing django to setup
        get_wsgi_application()

    def validate(self):
        super().validate()
        manage_py_path = os.path.join(self.target_dir, "manage.py")
        if not os.path.exists(manage_py_path):
            raise DjangoParserError(
                DjangoParserError.NOT_A_DJANGO_PROJECT.format(manage=manage_py_path)
            )
