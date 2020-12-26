"""Utility module to help configure the logger
on a Flask app.

Resources:

1. https://flask.palletsprojects.com/en/1.1.x/logging/
2. https://docs.python.org/3/library/logging.handlers.html
3. https://realpython.com/python-logging/#the-logging-module
"""

import logging
import logging.handlers

import flask
from flask.logging import default_handler


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if flask.has_request_context():
            record.url = flask.request.url
            record.remote_addr = flask.request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


def register_loggers(app: flask.Flask, stream=True, log_file=None, custom_handlers=None, **kwargs):
    """Registers custom handlers on the flask logger.

        Parameters:
            app:            Flask app
            stream:         Add StreamHandler. Default: True
            log_file:       Path for the TimedRotatingFileHandler file.
            custom_handlers:    List of additional handlers.

        Keyword Arguments:
            formatter_string:   A formatter string to apply for all the handlers.
            stream_handler_level: Level for the stream handler. Default is logging.warning.
            file_handler_level: Level for the file handler. Default: logging.DEBUG
            keep_default_handler: Default: False. Choose whether to keep the default log handler that Flask uses.
    """

    formatter = RequestFormatter(
        kwargs.get(
            "formatter_string",
            (
                "[%(asctime)s] %(remote_addr)s requested %(url)s\n"
                "%(levelname)s in %(module)s: %(message)s"
            )
        )
    )

    if stream:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(kwargs.get("stream_handler_level", logging.WARNING))
        stream_handler.setFormatter(formatter)

        app.logger.addHandler(stream_handler)

    if log_file is not None:
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=log_file, when="W0", interval=1, backupCount=4, utc=True, )
        file_handler.setLevel(kwargs.get("file_handler_level", logging.DEBUG))
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

    if custom_handlers is not None:
        for handler in custom_handlers:
            handler.setFormatter(formatter)
            app.logger.addHandler(handler)

    if not kwargs.get("keep_default_handler"):
        app.logger.removeHandler(default_handler)
