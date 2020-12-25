import dash


def register_dash_app(app, **kwargs):
    """Registers a dash application given a flask app"""
    if (endpoint := kwargs.get("dash_suffix")):
        dash_app = dash.Dash(__name__, server=app,
                             url_base_pathname=endpoint)
    else:
        dash_app = dash.Dash(__name__, server=app)
    app.dash_app = dash_app
