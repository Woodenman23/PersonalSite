from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint("views", __name__)


# define routes to webpages using 'views' blueprint
@views.route("/")
def home():
    return render_template("home.html")


@views.route("/joebird")
def joebird():
    return render_template("joebird.html")


@views.route("/gallery")
def gallery():
    return render_template("gallery.html")


@views.route("/projects")
def projects():
    return render_template("projects.html")


@views.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("views.user", usr=user))
    else:
        return render_template("login.html")


@views.route("/<usr>")
def user(usr):
    return f"user is {usr}."


@views.route("/<name>")
def say_hello(name):
    # return f'Hello {name}, welcome to my website! <a href="/">Go home</a>'
    return render_template("name.html", name=name)
