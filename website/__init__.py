from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path

# initialise database object
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234'
    app.config["SQLALCHEMY_DATABASE_URI" ] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # import blueprint so that app knows available routes
    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix='/')

    create_database(app)

    return app

def create_database(app: Flask) -> None:
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
