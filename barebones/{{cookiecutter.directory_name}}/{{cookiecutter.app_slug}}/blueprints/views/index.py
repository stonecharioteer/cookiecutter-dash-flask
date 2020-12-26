from flask.views import MethodView
from flask import current_app, jsonify

class IndexView(MethodView):
    def get(self, id):
        """GET route"""
        if id is None:
            current_app.logger.debug("Processing a GET request")
            return "Hello, world", 200
        else:
            current_app.logger.debug("A user has requested info regarding %d", id)
            return f"Hello, {id}", 200

    def post(self, id):
        if id is None:
            current_app.logger.warning("The `id` is None.")
            return jsonify(dict(message="Error, ID is needed for POST")), 401
        elif id == 0:
            try:
                1/id
            except ZeroDivisionError:
                current_app.logger.error("ID cannot be Zero!", exc_info=True)
                return jsonify(dict(message="Error, ID cannot be Zero, the server has an error.")), 422
        elif id == 43:
            current_app.logger.critical("Critical error! 43 is not the answer!")
            return jsonify(dict(message="Error. This is not the answer")), 500

        return f"Processed {id}", 200
