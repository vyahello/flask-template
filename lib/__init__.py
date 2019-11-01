from flask import render_template, Flask

app = Flask(__name__)

from lib import routes
