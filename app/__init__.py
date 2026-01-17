from flask import Flask
from .routes.home import home_page

app = Flask(__name__)
app.register_blueprint(home_page)

if __name__ == "__main__":
    app.run()