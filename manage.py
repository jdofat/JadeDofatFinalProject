#!/usr/bin/env python3

# run this file to start the Django project
# tells Django to use settings file to use
# runs terminal commands
# launches the website

import os
import sys

def main():
    # sets the settings file for the project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internshipfinder.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "couldn't import django, need to install."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
