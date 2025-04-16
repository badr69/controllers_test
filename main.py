from flask import Flask
from app.routes.auth_routes import auth_bp


# Importer les autres blueprints

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    app.register_blueprint(auth_bp)
    # Register other routes...

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
