from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_PATH = PROJECT_ROOT / "website/static/images"


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "1234"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///users.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # import blueprint so that app knows available routes
    from .views import views

    # from .auth import auth

    # app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    # db = SQLAlchemy(app)

    # # Table in database
    # class Users(db.Model):
    #     _id = db.Column("id", db.Integer, primary_key=True)  # column 1
    #     name = db.Column("name", db.String(100))
    #     email = db.Column("email", db.String(100))

    #     def __init__(self, name, email) -> None:
    #         self.name = name
    #         self.email = email

    # db.create_all()

    return app


# def create_database(app: Flask) -> None:
#     db = SQLAlchemy()
#     DB_NAME = "database.db"
#     if not path.exists("website/" + DB_NAME):
#         db.create_all(app=app)
#         print("Created Database!")
