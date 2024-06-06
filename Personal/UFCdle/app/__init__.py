from flask import Flask
from .routes import bp as routes_bp
from .db import close_db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp)

    @app.teardown_appcontext
    def teardown_db(exception):
        close_db(exception)

    return app
