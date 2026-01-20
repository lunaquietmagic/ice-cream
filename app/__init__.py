from flask import Flask
from config import config

from .routes.home import home_page
from .routes.login import login_page
from .routes.profile import profile_page
from .routes.register import register_page
from .routes.chat import chat_page

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(home_page)
    app.register_blueprint(login_page)
    app.register_blueprint(profile_page)
    app.register_blueprint(register_page)
    app.register_blueprint(chat_page)

    return app