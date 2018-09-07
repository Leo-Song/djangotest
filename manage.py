#!/usr/bin/env python
import os
import sys

<<<<<<< HEAD
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LeoBlog.settings')
=======
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LeoBlog.settings")
>>>>>>> 391104e34022b0255ff7347de6834b45f75c14ae
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

