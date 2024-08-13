from flask import Blueprint, render_template, request, session, redirect, url_for, flash

views = Blueprint("views", __name__)


# define routes to webpages using 'views' blueprint
@views.route("/")
def home():
    return render_template("home.html.j2")


@views.route("/joebird")
def joebird():
    return render_template("joebird.html.j2")


@views.route("/gallery")
def gallery():
    return render_template("gallery.html.j2")


@views.route("/projects")
def projects():
    return render_template("projects.html.j2")


@views.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        session["logged_in"] = True
        flash("Login successful!", "success")
        return redirect(url_for("views.user"))
    else:
        if "user" in session:
            flash("Already logged in!", "info")
            return redirect(url_for("views.user"))
        return render_template("login.html.j2")


@views.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html.j2", user=user)
    else:
        return redirect(url_for("views.login"))


@views.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
        session.pop("logged_in", None)
        flash("You are now logged out.", "info")
    return render_template("login.html.j2")
