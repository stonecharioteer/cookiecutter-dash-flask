# {{ cookiecutter.app_name }}


{{ cookiecutter.app_description }}

## Installation

```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements_dev.txt
```

## Deployment

To deploy this application, use `gunicorn`.

```bash

gunicorn -w 10 -b localhost:1000 wsgi:app

```

## Configuration

This application follows a modular configuration system, as detailed in [Explore Flask](https://exploreflask.org).

Create `instance/config.py` or set an environment variable `{{ cookiecutter.app_name|upper}}_CONFIG` to point to a config. You may use `config/instance_template.py` as a template to help you create that file.

Additionally, all environment variables using the `{{ cookiecutter.app_name|upper}}_` prefix will be read and the appropriate configuration variables will be overwritten.

Example: setting `{{ cookiecutter.app_name|upper}}_LOGFILE` will overwrite the value of the `LOGFILE` variable.


## Extending the API

{{ cookiecutter.app_name }} provides both a Flask API and a Dash Web UI. This separation enables users to develop an application whose backend and frontend are independent, should they choose to later separate the repo entirely, that will help them do so.

### Adding New Pages to the GUI

<!-- TODO: Explain how to add new pages to the GUI here -->

### Adding New Routes to the API

#### Adding New Routes to the `core` Blueprint

<!-- TODO: Explain how to add new routes to the API -->

#### Adding New Blueprints


### Writing Backend Tests

### Writing Frontend Tests
