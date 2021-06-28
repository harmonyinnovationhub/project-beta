from core import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_Name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    files = db.relationship('File', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.company_Name}', '{self.email}' )"


#File Table
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.LargeBinary, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_Metadatas = db.relationship('File_metadata', backref='uploadedFile', lazy=True)

    def __repr__(self):
        return f"File('{self.id}', )"

# Metadata table
class File_metadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_Name = db.Column(db.String(20), nullable=False)
    file_Type = db.Column(db.String(10), nullable=False)
    file = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)

    def __repr__(self):
        return f"File_metadata({self.file_Name}, {self.file_Type})"

