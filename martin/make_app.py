import os

from flask import Flask
from flask.ext.iniconfig import INIConfig
from flask_security import SQLAlchemyUserDatastore
from flask_admin.contrib.sqla import ModelView
from martin.models import db, security, admin
from martin.models.users import Role, User


def make_app(*args, **kwargs):
    app = Flask(__name__)
    INIConfig(app)
    app.config['APP_PATH'] = os.path.dirname(
        os.path.abspath(__file__))
    app.config['CFG_PATH'] = os.path.join(
        app.config['APP_PATH'], 'configurations', 'local.ini')
    app.config.from_inifile_sections(app.config['CFG_PATH'],
                                     ['app:flask'])
    db.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    return app
