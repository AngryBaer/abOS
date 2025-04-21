"""
    Launch app from the command line.
"""
import argparse
from .core import run_app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Launch app from the command line.',
        prog='abLaunch',
        usage='%(prog)s [app] [mode]',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('app', help='The name of the app.')
    parser.add_argument('--dev', help='run in dev mode', action='store_true')
    args = parser.parse_args()

    run_app(args.app, args.dev)
