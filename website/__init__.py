from flask import Flask
from flask_scss import Scss
from flask_mail import Mail
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_PATH = PROJECT_ROOT / "website/static/images"
USER_HOME = Path.home()
MODEL_PATH = USER_HOME / "models/dognet-convnext_large.pth"

# Initialize Flask-Mail globally
mail = Mail()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "1234"
    
    # Email configuration
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

    # Initialize extensions
    mail.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app
