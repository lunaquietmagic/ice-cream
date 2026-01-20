from flask import Blueprint, render_template

register_page = Blueprint('register__page', __name__)

@register_page.route("/register")
def register():
    return render_template("register.html")