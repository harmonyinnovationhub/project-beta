from os import name
from flask import Flask, jsonify, json, request, make_response
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from core import app
from models import db, User, LogLag

# creating new users
@app.route('/register', methods=['POST', "GET"])
def create_user():
    data = json.loads(request.data, strict=False)
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(token=str(uuid.uuid4()),
                    name=data['name'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "New User Created"})

# Login user
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'token': user.token}, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


@app.route('/submit', methods=['POST'])
def submit():
    data = json.loads(request.data, strict=False)
    new_loglat = LogLag(logitude=data['logitude'], latitude=data['latitude'])
    db.session.add(new_loglat)
    db.session.commit()
    return jsonify({"message": "Logititude and Latitude submitted successfully"})
    
@app.route('/retrieve', methods=['GET'])
def getLogLat():
    data = json.loads(request.data, strict=False)
    resultt = LogLag.query.all()
    #jj = resultt.dump(LogLag.query.all())
    return jsonify( resultt)
