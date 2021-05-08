from flask import Flask
from flask_cors import CORS


def create_app():
    from . import routes
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    routes.init_app(app)
    return app
