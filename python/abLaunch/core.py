"""
    Run app in a subprocess.
"""
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

    subprocess.run(configuration.executable, check=True, shell=True)
