from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_admin import Admin

db = SQLAlchemy()
security = Security()
admin = Admin(name='martin', template_mode='bootstrap3')
