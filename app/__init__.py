from flask import Flask

from .routes.home import home_page
from .routes.login import login_page
from .routes.profile import profile_page
from .routes.register import register_page

app = Flask(__name__)

app.register_blueprint(home_page)
app.register_blueprint(login_page)
app.register_blueprint(profile_page)
app.register_blueprint(register_page)


if __name__ == "__main__":
    app.run()