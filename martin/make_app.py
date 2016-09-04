import os

from flask import Flask
from flask_iniconfig import INIConfig
from flask_security import SQLAlchemyUserDatastore
from flask_admin.contrib.sqla import ModelView
from martin.models import db, security, admin
from martin.models.users import Role, Users
from martin.controllers.index import IndexBlueprint


def make_app(*args, **kwargs):
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='')
    INIConfig(app)
    app.config['APP_PATH'] = os.path.dirname(
        os.path.abspath(__file__))
    app.config['CFG_PATH'] = os.path.join(
        app.config['APP_PATH'], 'configurations', 'local.ini')
    app.config.from_inifile_sections(app.config['CFG_PATH'],
                                     ['app:flask'])
    db.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, Users, Role)
    security.init_app(app, user_datastore)
    admin.init_app(app)
    admin.add_view(ModelView(Users, db.session))

    app.register_blueprint(IndexBlueprint)
    return app
