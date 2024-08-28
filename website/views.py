from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from wikipedia.exceptions import DisambiguationError

from website import IMAGES_PATH
from website.wiki_search import wiki_summary
from website.country import Country
from website.projects import Project
from website.entities import Skill, Image, skill_urls

views = Blueprint("views", __name__)

LOGO_URLS = {
    "hostel_world": "https://a.hwstatic.com/raw/upload/f_auto,q_auto/wds/logos/brand/hw-orange.svg"
}

PROJECTS = ["virtual_assistant", "yoga_sequence", "hangman"]

COUNTRIES = [
    "egypt",
    "australia",
    "guatemala",
    "mexico",
    "india",
    "japan",
    "peru",
    "thailand",
    "cyprus",
    "israel",
    "belgium",
    "france",
    "italy",
    "switzerland",
    "canada",
    "cambodia",
    "vietnam",
    "turkey",
    "wales",
    "scotland",
    "england",
    "bahrain",
    "nepal",
    # "USA",
    "netherlands",
]

SKILLS = skill_urls.keys()


@views.route("/")
def home():
    skills = [Skill(skill) for skill in SKILLS]
    return render_template("home.html.j2", skills=skills)


@views.route("/travel", methods=["POST", "GET"])
def travel():
    if request.method == "POST":
        country = request.form["country"]
        return redirect(url_for("views.country", country_name=country))
    files = IMAGES_PATH.glob("*")
    images = [file.name for file in files if file.is_file()]
    countries = [Country(country) for country in COUNTRIES]
    return render_template("travel.html.j2", countries=countries, images=images)


@views.route("/images/<category>/<image_name>")
def image(image_name: str, category: str) -> None:
    image = Image(image_name, category)
    return render_template("image.html.j2", image=image)


@views.route("/country/<country_name>")
def country(country_name: str) -> str:
    country = Country(country_name)

    return render_template(
        "country.html.j2",
        country=country,
    )


@views.route("/gallery")
def gallery():
    files = IMAGES_PATH.glob("*")
    images = [file.name for file in files if file.is_file()]
    return render_template("gallery.html.j2", images=images)


@views.route("/projects")
def projects():
    projects = [Project(project) for project in PROJECTS]
    return render_template("projects.html.j2", projects=projects)


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


@views.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email saved.")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html.j2", user=user, email=email)
    else:
        return redirect(url_for("views.login"))


@views.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
        session.pop("logged_in", None)
        session.pop("email", None)
        flash("You are now logged out.", "info")
    return render_template("home.html.j2")


@views.route("/ask", methods=["POST", "GET"])
def ask():
    if request.method == "POST":
        search_term = request.form["search_term"]
        try:
            result = wiki_summary(search_term)
        except DisambiguationError:
            return no_result(search_term)
        if result == None:
            return no_result(search_term)
        return render_template("answer.html.j2", search_term=search_term, result=result)
        # TODO: handle API connection error
    else:
        return render_template("questions.html.j2")


def no_result(search_term: str) -> str:
    return render_template(
        "answer.html.j2",
        search_term=search_term,
        result="I cannot summarize this, try something else.",
    )
