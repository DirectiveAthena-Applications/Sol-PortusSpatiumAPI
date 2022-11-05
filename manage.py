# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import sys
from django.core.management import execute_from_command_line

# Athena Packages
from AthenaLib.parsers.dot_env import DotEnv

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    """Run administrative tasks."""
    # Gather all env variables from the secrets folder
    DotEnv("secrets/portus_spatium_api.env", auto_run=True)

    # Django do stuff
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
