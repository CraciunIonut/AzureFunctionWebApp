from flask import Blueprint, render_template

blueprintMain = Blueprint('mainMethod', __name__)

@blueprintMain.route('/')
def main():
    return render_template("mainpage.html")
    