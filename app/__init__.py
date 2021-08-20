from flask import Flask, request, g
from flask_babel import Babel, _

from .config import Config

lang_code = 'en'

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

babel = Babel(app)

@babel.localeselector
def get_locale():
	return request.json["lang"]