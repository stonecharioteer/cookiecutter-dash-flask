import dash
import dash_html_components as html
from .callbacks import register_callbacks
from .components import (
    get_location,
    get_interval,
    get_notification_area,
    get_navbar,
    get_sidebar,
    get_body,
    get_footer,
    get_login_form,
    get_page_1,
    get_page_2,
    get_page_404,
)

from .utils import encode_state, decode_state


class DashApp:
    def __init__(self, flask_app, name, title):
        self.flask_app = flask_app
        self.app = dash.Dash(
            name,
            server=self.flask_app,
        )
        self.app.title = title
        with self.flask_app.app_context():
            self.location = get_location()
            self.interval = get_interval()
            self.navbar = get_navbar()
            self.notification_area = get_notification_area()
            self.sidebar = get_sidebar()
            self.page_1 = get_page_1()
            self.page_2 = get_page_2()
            self.body = get_body()
            self.footer = get_footer()
            self.app.layout = self.get_layout()
            register_callbacks(self.app)

    def get_layout(self):

        self.app.validation_layout = self.get_validation_layout()
        base_layout = html.Div([
            self.location,
            self.interval,
            self.navbar,
            self.notification_area,
            self.sidebar,
            self.body,
            self.footer,
        ])
        return base_layout

    def get_validation_layout(self):
        """Vaidation layout is how dash deals with being able to map events
        to invisible components that may not yet have rendered onto the canvas
        of a multipage application.

        Add all components which have callbacks here. This will enable
        the events to work as expected."""
        validation_layout = html.Div(children=[
            self.location,
            self.interval,
            self.navbar,
            self.notification_area,
            self.sidebar,
            self.body,
            self.footer,
            self.page_1,
            self.page_2,
            self.page_3,
        ])
        return validation_layout
