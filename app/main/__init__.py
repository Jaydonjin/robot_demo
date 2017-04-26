from flask import Blueprint

url_prefix = '/robot_demo'
main = Blueprint('main', __name__, url_prefix=url_prefix)

from . import views
