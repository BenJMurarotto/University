from flask import Flask
from flask_cors import CORS
from flask_session import Session
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'  # Replace with a strong, unique key
    app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem to store session data
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True  # Sign the session data
    app.config['SESSION_FILE_DIR'] = os.path.join(app.instance_path, 'flask_session')  # Directory to store session files

    # Create the session directory if it doesn't exist
    os.makedirs(app.config['SESSION_FILE_DIR'], exist_ok=True)

    Session(app)
    CORS(app)  # This will enable CORS for all routes

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
