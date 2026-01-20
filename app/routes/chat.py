from flask import Blueprint, render_template

chat_page = Blueprint('chat_page', __name__)

@chat_page.route("/chat")
def view_chat():
    return render_template("chat.html", page_name="chat")