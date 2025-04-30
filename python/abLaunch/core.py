"""
    Run app in a subprocess.
"""
import os
import subprocess
from abEnvs import EnvSetup, EnvMode


def run_app(app_name: str, dev: bool = False):
    """ Run the given app in a subprocess. """
    if dev:
        mode = EnvMode.DEV
    else:
        mode = EnvMode.PROD

    configuration = EnvSetup(app_name, mode)
    configuration.setup_envs()
    configuration.setup_paths()

    command = f'"{configuration.executable}" {configuration.args_string}'
    subprocess.run(command, check=True, shell=True)


if __name__ == "__main__":
    run_app("blender", dev=True)
