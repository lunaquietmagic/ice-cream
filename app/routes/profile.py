from flask import Blueprint, render_template

profile_page = Blueprint('profile_page', __name__)

@profile_page.route("/profile")
def profile():
    return render_template("profile.html", page_name="profile")