"""robot_demo

"""

from flask import Flask
from nlog import NLog


__version__ = '0.0.1'
__author__ = 'DAE'


def create_app(config_name):
    app = Flask(__name__, static_url_path='/robot_demo/static')
    app.config.from_object('config.default')
    config_name_lower = config_name.lower()
    app.config.from_object('config.{0}'.format(config_name_lower))
    app.config['VERSION'] = __version__
    project_env = "gdev" if config_name_lower == 'development' else config_name_lower

    NLog("robot_demo",
         logger=app.logger,
         level=app.config.get('LOG_LEVEL', 'info'),
         console=app.config.get('LOG_ENABLE_CONSOLE', True),
         bts=app.config.get('LOG_ENABLE_CONSOLE', True), env=project_env, global_name='dae')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
