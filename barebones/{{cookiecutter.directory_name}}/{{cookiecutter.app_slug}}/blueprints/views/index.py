from flask.views import MethodView


class IndexView(MethodView):
    def get(self, id):
        """GET route"""
        if id is None:
            return "Hello, world", 200
        else:
            return f"Hello, {id}", 200

    def post(self, id):
        return f"Processed {id}", 200
