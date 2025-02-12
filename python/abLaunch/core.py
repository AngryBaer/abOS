"""
    Run app in a subprocess.
"""

import subprocess
from abEnvs import EnvSetup


def run_app(app_name: str):
    """ Run the given app in a subprocess. """
    configuration = EnvSetup(app_name)
    configuration.setup_envs()
    configuration.setup_paths()

    subprocess.run(configuration.executable, check=True, shell=True)
