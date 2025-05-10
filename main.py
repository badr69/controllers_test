from flask import Flask, render_template
from app.models.db import Connexion
from app.routes.user_routes import user_bp
app = Flask(__name__)
app.register_blueprint(user_bp)

@app.route('/')
def index():
    return "Bienvenue dans l'application de covoiturage!"
@app.route('/register')
def register():
    return render_template("register.html")

@app.teardown_appcontext
def close_db_connection(exception=None):
    Connexion.close_all_connections()
