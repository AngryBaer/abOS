"""
    Manage app environment variables.
"""
import os
import re
import sys
import abJSON

ENVCONFIGS = os.path.join(os.path.dirname(__file__), "configs")
ENVCOMMON = os.path.join(ENVCONFIGS, "common.json")


class EnvSetup():
    """ App env vars setup. """

    def __init__(self, config_name: str) -> None:
        self.__paths = []
        self.__common = abJSON.read(ENVCOMMON)
        self.__config = self.parse_configs(config_name)

    @property
    def executable(self) -> os.PathLike:
        """ Return path to executable file. """
        return self.__config.get("executable")

    def setup_envs(self):
        """ Set Environment variables. """
        os.environ.update(self.__common)

    def setup_paths(self):
        """ Set Python paths. """
        os.environ["PYTHONPATH"] = ';'.join(self.__paths)
        sys.path.extend(self.__paths)

    def parse_configs(self, config_name: str) -> dict:
        """ Read configuration files. """
        config_file = os.path.join(ENVCONFIGS, f"{config_name}.json")
        config_data = abJSON.read(config_file)

        for dependency in config_data.get("dependencies", []):
            self.parse_configs(dependency)

        for token, root in self.__common.items():
            for python_path in config_data.get("PYTHONPATH", []):
                self.__paths.append(os.path.abspath(re.sub(token, root, python_path)))

        return config_data
