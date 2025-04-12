from .controllers import auth_controller, ride_controller
from flask import redirect

def init_routes(app):
    app.add_url_rule("/", view_func=lambda: redirect("/login"))
    app.add_url_rule("/login", view_func=auth_controller.login, methods=["GET", "POST"])
    app.add_url_rule("/register", view_func=auth_controller.register, methods=["GET", "POST"])
    app.add_url_rule("/rides", view_func=ride_controller.list_rides)
    app.add_url_rule("/add_ride", view_func=ride_controller.add_ride, methods=["GET", "POST"])