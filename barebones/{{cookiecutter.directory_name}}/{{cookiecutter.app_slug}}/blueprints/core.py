"""Core blueprint"""
from flask import Blueprint
from .views import IndexView

from .register import create_blueprint_view_registrar


core = Blueprint("core", import_name="core")

# create a registrar function from the helper function in
# `{{ cookiecutter.app_slug }}.blueprints.register.py`
register_view = create_blueprint_view_registrar(core)

# Create a list of dictionaries which have `methods`, `url`, and (optionally) `defaults`
# as the keys.
register_view_url_rules = [
    {
        "methods": ["GET"],
        "url": "/",
        "defaults": {"id": None},
    },
    {
        "methods": ["GET", "POST"],
        "url": "/<int:id>",
    }
]

# register the IndexView
register_view(IndexView, "index_view", "/", url_rules=register_view_url_rules)
