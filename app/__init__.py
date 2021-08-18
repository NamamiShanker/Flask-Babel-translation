from flask import Flask, request
from flask_babel import Babel, _

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

babel = Babel(app)

@babel.localeselector
def get_locale():
	# return 'es'
	return request.accept_languages.best_match(app.config['LANGUAGES'])
