from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://beta:password@localhost/beta'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import views