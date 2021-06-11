from core import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# user table


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean)

class LogLag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logitude = db.Column(db.Float(128))
    latitude = db.Column(db.Float(128))

    def __init__(self, logitude, latitude):
        self.logitude = logitude
        self.latitude = latitude

