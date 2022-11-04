from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

from Controlador.ControladorCandidato import ControladorCandidato
from Controlador.ControladorMesa import ControladorMesa
miControladorCandidato=ControladorCandidato()
miControladorMesa=ControladorMesa()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running..."
    return jsonify(json)

@app.route("/candidato",methods=['GET'])
def getEstudiantes():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidato",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorCandidato.show(id)
    print(json)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

"""Implementacion metodo main para mesas"""

@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
