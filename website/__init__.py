from flask import Flask
from flask_scss import Scss
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_PATH = PROJECT_ROOT / "website/static/images"
USER_HOME = Path.home()
MODEL_PATH = USER_HOME / "models/dognet-convnext_large.pth"


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "1234"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
