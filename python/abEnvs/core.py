"""
    Manage app environment variables.
"""
import os
import re
import sys
import enum

import abJSON


ENVCONFIGS = os.path.join(os.path.dirname(__file__), "configs")
ENVCOMMON = os.path.join(ENVCONFIGS, "common.json")


class EnvMode(enum.Enum):
    """ Enum for environment variable modes. """

    def __str__(self):
        return self.value

    DEV = "AB_DEVELOPMENT"
    PROD = "AB_PRODUCTION"


class EnvKeys(enum.Enum):
    """ Enum for environment config keys. """

    def __str__(self):
        return self.value

    PATH = "PYTHONPATH"
    ROOT = "ENV_ROOT"
    TOKEN = "ENV_TOKEN"
    DEPEND = "dependencies"
    EXEC = "executable"
    ARGS = "args"


class EnvSetup():
    """ App environment variables setup. """

    COMMON = abJSON.read(ENVCOMMON)

    def __init__(self, app_name: str, mode: EnvMode = EnvMode.PROD) -> None:
        self.__mode = str(mode)
        self.__root = self.COMMON[self.__mode][str(EnvKeys.ROOT)]
        self.__token = self.COMMON[self.__mode][str(EnvKeys.TOKEN)]

        self.__path = []
        self.__args = []
        self.__config = self.parse_configs(app_name)

    @property
    def executable(self) -> os.PathLike:
        """ Return path to executable file. """
        return os.path.abspath(self.__config.get(str(EnvKeys.EXEC)))

    @property
    def args(self) -> list:
        """ Return all launch arguments. """
        return self.__args

    @property
    def args_string(self) -> str:
        """ Return all launch arguments as string. """
        return ' '.join(self.args)

    def setup_envs(self) -> None:
        """ Set global environment variables. """
        for key, value in self.COMMON[self.__mode].items():
            os.environ[key] = str(value)

    def setup_paths(self) -> None:
        """ Set Python paths. """
        os.environ[str(EnvKeys.PATH)] = ';'.join(self.__path)
        sys.path.extend(self.__path)

    def parse_configs(self, config_name: str) -> dict:
        """ Read configuration files. """
        config_data = abJSON.read(os.path.join(ENVCONFIGS, f"{config_name}.json"))

        # recursively parse all dependencies
        for dependency in config_data.get(str(EnvKeys.DEPEND), []):
            self.parse_configs(dependency)

        # parse all path dependencies
        for python_path in config_data.get(str(EnvKeys.PATH), []):
            self.__path.append(os.path.abspath(re.sub(self.__token, self.__root, python_path)))

        # parse launch arguments
        for flag in config_data.get(str(EnvKeys.ARGS), []):
            self.__args.append(flag)

        return config_data
