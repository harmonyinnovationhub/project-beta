from flask import jsonify, json, request

from core import app
# from models import db
# , LogLag


# @app.route('/submit', methods=['POST'])
# def submit():
#     data = json.loads(request.data, strict=False)
#     new_loglat = LogLag(logitude=data['logitude'], latitude=data['latitude'])
#     db.session.add(new_loglat)
#     db.session.commit()
#     return jsonify({"message": "Logititude and Latitude submitted successfully"})
    
# @app.route('/retrieve', methods=['GET'])
# def getLogLat():
#     location = []
#     data = json.loads(request.data, strict=False)
#     resultt = LogLag.query.filter_by(logitude=data['logitude'], latitude=data['latitude'])
#     for log in resultt:
#         logi = log.logitude
#         lati = log.latitude
#         result = {
#             "Requested logitude" : logi,
#             "Requested latitude ": lati
#         }
#         location.append(result)
#     return jsonify(location)
    
    
