
def create_blueprint_view_registrar(blueprint):
    """returns a function that will register an endpoint
    with a method view.

    See https://flask.palletsprojects.com/en/1.1.x/views/#method-views-for-apis
    for details. This is a modified version of the helper that appears there.
    """
    def register_api(view, endpoint, url, url_rules):
        """This function registers a flask.views.MethodView atop an endpoint."""
        view_func = view.as_view(endpoint)
        for rule in url_rules:
            methods = rule["methods"]
            url = rule["url"]
            defaults = rule.get("defaults")
            if defaults is not None:
                blueprint.add_url_rule(
                    url, defaults=defaults, view_func=view_func, methods=methods)
            else:
                blueprint.add_url_rule(
                    url, view_func=view_func, methods=methods)
    return register_api
