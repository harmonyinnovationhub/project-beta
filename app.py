from enum import unique
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from sqlalchemy.sql.functions import user
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://beta:password@localhost/beta'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     full_name = db.Column(db.String(50))
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     pass_w = db.Column(db.String(50))
    


#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

    
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    full_name = StringField('Fullname', [validators.DataRequired(), validators.Length(min=3, max=35)]) 
    email = StringField('email', [validators.DataRequired(), validators.Length(min=3, max=35)])
    username = StringField('username',[validators.DataRequired(), validators.Length(min=3, max=35)])
    pass_w = PasswordField('password', [validators.DataRequired(), validators.Length(min=3, max=35)])



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
   
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user= User( email=form.email.data, username=form.username.data, pass_w=form.pass_w.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user has been created </h1>'
    
    return  render_template('register.html', form=form)

# @app.route('/form', methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#         details = request.form
#         firstName = details['users_name']
#         lastName = details['users_email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO users(users_name, users_email) VALUES (%s, %s)", (firstName, lastName))
#         mysql.connection.commit()
#         cur.close()
#         return 'success'
#     return render_template('form.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001", debug = True)