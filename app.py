from flask import *
from flask.ext.login import (LoginManager, login_user, logout_user,
                             login_required, current_user)
from peewee import *
from playhouse.flask_utils import FlaskDB

site = Flask(__name__)
site.config.from_object('settings')

flask_db = FlaskDB(site)
database = flask_db.database

login_manager = LoginManager()
login_manager.init_app(site)
login_manager.login_view = 'login'
