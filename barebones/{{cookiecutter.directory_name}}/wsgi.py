from {{ cookiecutter.app_slug }} import create_app

# if you'd like to use an instance folder, then copy the `config/instance_template.py`
# file and edit all the placeholder values.

app = create_app(config_file="config.py")
