# Cookiecutter Templates for a Dash Web Application

This repo contains several cookiecutter templates, all of them targetting `dash`-based Flask Web applications.

## Goal

With these templates you should be able to create the following sorts of projects

1. `barebones`

    This is a project that uses dash, has a header and a footer, and a multipage view setup.
    The application has a separate Flask API, and allows registration of additional blueprints.

2. `authentication`

    This is similar to the previous application but also provides authentication. It uses `flask-sqlalchemy` for the database connections.

3. `fastapi`

    This is a version of `barebones` that uses `fast-api` instead of `flask` for the backend.
    It accordingly uses `uvicorn` instead of `gunicorn` for deployment.


## Usage

Run:

`cookiecutter gh:stonecharioteer/cookiecutter-dash-flask --directory=barebones`

You can choose the directory name depending on the type of webapp you'd like.
