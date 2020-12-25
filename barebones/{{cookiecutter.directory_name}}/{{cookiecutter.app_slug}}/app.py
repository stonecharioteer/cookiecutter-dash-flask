"""Application Factory for {{ cookiecutter.app_name }}"""
import os

from flask import Flask
import dash


def create_app(config=None, config_file=None, **kwargs):
    """application factory

        Parameters:
            config: Configuration object, importable.
                    The options are `config.<filename>`
                    Note that the `.py` suffix is not necessary.
            config_file: path to a config file

        Keyword Parameters:
            configure_dash: Flag to forgo the registration of the Dash API.
                            This is useful during testing.

                            Additionally, any kwargs that are prefixed with
                            `{{ cookiecutter.app_slug|upper }}_`
                            are used to override the corresponding
                            application config variables.

        Configuration:
            See notes in the README.md file.
    """

    app = Flask(__name__, instance_relative_config=True)
    # load the base config
    app.config.from_object("config.base")

    # load the config from an object
    if config is not None:
        app.config.from_object(config)

    if config_file is not None:
        app.config.from_pyfile(config_file)

    config_prefix = "{{ cookiecutter.app_slug|upper }}_"
    # If the {{ cookiecutter.app_slug|upper }}_CONFIG is defined,
    # then load that file as well.
    if (env_file := os.getenv(f"{config_prefix}CONFIG")) is not None:
        app.config.from_pyfile(env_file)

    # override the configuration values using environment variables
    # that are prefixed with `{{ cookiecutter.app_slug|upper }}_`

    config_envvars = dict(
        (key, value) for key, value in
        os.environ.items() if key.startswith(config_prefix)
    )

    for key, value in config_envvars:
        config_name = key[len(config_prefix):]
        value = value.strip()
        if value.isdigit():
            value = int(value)
        elif value.isdecimal():
            value = float(value)
        app.config[config_name] = value

    # configure the dash application
    if kwargs.get("configure_dash", True):
        from .ui import register_dash_app
        register_dash_app(app, **kwargs)

    # register the blueprints
    from .blueprints import core

    app.register_blueprint(core, url_prefix="/api/v1")

    return app
