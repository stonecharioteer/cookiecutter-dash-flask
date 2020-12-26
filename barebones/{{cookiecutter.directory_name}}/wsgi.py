
import pathlib

from {{ cookiecutter.app_slug }} import create_app

# if you'd like to use an instance folder, then copy the `config/instance_template.py`
# file and edit all the placeholder values.

config_file = pathlib.Path("instance/config.py")
if not config_file.is_file():
    raise EnvironmentError("The config file {} does not exist".format(config_file.absolute()))

app = create_app(config_file=config_file.absolute())
