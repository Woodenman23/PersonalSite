from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# define routes to webpages using 'views' blueprint
@views.route('/')
def home():
    return render_template('home.html')

@views.route("/joebird")
def joebird():
    return render_template("joebird.html")

@views.route("/gallery")
def gallery():
    return render_template("gallery1.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")