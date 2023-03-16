from flask import Flask

from app.config import config


def create_app(config_name='default'):
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config.from_object(config[config_name])

    from app.main import main

    app.register_blueprint(main)

    return app

