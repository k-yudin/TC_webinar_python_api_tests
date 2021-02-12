import os


class Environment:
    def __init__(self):
        self.domain = self._get_environment_variable()

    @classmethod
    def _get_environment_variable(cls) -> str:
        try:
            return os.environ['PYTEST_DOMAIN']
        except KeyError:
            return "http://localhost"

    def base_url(self) -> str:
        return self.domain


ENV = Environment()
