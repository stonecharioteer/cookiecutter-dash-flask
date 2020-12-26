"""This is the gunicorn config file.

Gunicorn will use this file when you run it from a folder containing it.

See: https://docs.gunicorn.org/en/latest/settings.html#settings to learn
how to write this file

The defaults here are what help devs debug problems
"""

import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = "wsgi:app"
reload = True
