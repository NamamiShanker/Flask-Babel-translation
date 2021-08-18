from flask import render_template
from app import app
from flask_babel import _

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')