#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

from django.conf import settings

logging.basicConfig(level=logging.INFO, format='\n \033[92m %(message)s \033[0m \n')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

    # debug
    if os.environ.get('RUN_MAIN') and settings.APP_ENV == 'local':
        import ptvsd
        logging.info('DEBUG SERVER STARTED AT PORT 3000')
        ptvsd.enable_attach(address=('0.0.0.0', 3000))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
