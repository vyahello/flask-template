from flask import render_template, request, Flask

app = Flask(__name__)

from src import routes
