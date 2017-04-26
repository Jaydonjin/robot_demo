from flask import render_template

from app.main import main
from app.models import Book


@main.route("/", methods=['GET'])
def index():
    return render_template('main/index.html')
