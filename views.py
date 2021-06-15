from flask import jsonify, json, request
from osgeo import gdal
import os
from werkzeug.utils import secure_filename


from core import app
from models import db, LogLag, Upload


@app.route('/submit', methods=['POST'])
def submit():
    data = json.loads(request.data, strict=False)
    new_loglat = LogLag(logitude=data['logitude'], latitude=data['latitude'])
    db.session.add(new_loglat)
    db.session.commit()
    return jsonify({"message": "Logititude and Latitude submitted successfully"})
    
@app.route('/retrieve', methods=['GET'])
def getLogLat():
    location = []
    data = json.loads(request.data, strict=False)
    resultt = LogLag.query.filter_by(logitude=data['logitude'], latitude=data['latitude'])
    for log in resultt:
        logi = log.logitude
        lati = log.latitude
        result = {
            "Requested logitude" : logi,
            "Requested latitude ": lati
        }
        location.append(result)
    return jsonify( location)

@app.route('/convert', methods=['POST'])
def gj():
    def shapefile2geojson(infile, outfile):
       options = gdal.VectorTranslateOptions(format="GeoJSON", dstSRS="EPSG:4326")
       gdal.VectorTranslate(outfile, infile, options=options)

    file = request.files['file']

    if not file:
        return 'No file attached', 400

    filemane = secure_filename(file.filename)
    mimetype = file.mimetype
    file = Upload(file=file.read(), mimetype=mimetype, name=filemane)
    db.session.add(file)
    db.session.commit()
    infile = 'shp/national_grid_group.shp'.strip('"')
    output_geojson = os.path.splitext(infile)[0] + ".geojson"

    shapefile2geojson(file, output_geojson)
    return {"convert": "Successfullly"}


# @app.route('/converttt', methods=['GET'])
# def shapefile2geo():
#     reader = shapefile.Reader("shp/national_grid_group.shp")
#     fields = reader.fields[1:]
#     field_names = [field[0] for field in fields]
#     buffer = []
#     for sr in reader.shapeRecords():
#         atr = dict(zip(field_names, sr.record))
#         geom = sr.shape.__geo_interface__
#         buffer.append(dict(type="Feature", \
#         geometry=geom, properties=atr)) 
    
#         # write the GeoJSON file
    
#     geojson = open("pyshp-demo.json", "w")
#     geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
#     geojson.close()
#     return {"jjjj" : geojson }

