from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

from Controlador.ControladorCandidato import ControladorCandidato
from Controlador.ControladorPartido import ControladorPartido
from Controlador.ControladorMesa import ControladorMesa
from Controlador.ControladorResultado import ControladorResultado

miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running..."
    return jsonify(json)


@app.route("/candidato", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    print(json)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
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


"""Implementacion metodo main para partidos"""


@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)


@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

"""Implementacion metodo main para resultados"""

@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)


@app.route("/resultados/partido/<string:id_partido>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def crearResultado(id_partido,id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.create(data,id_partido, id_candidato, id_mesa)
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>/partido/<string:id_partido>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def modificarResultado(id_resultado,id_partido, id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado, data,id_partido, id_candidato, id_mesa)
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>", methods=['DELETE'])
def eliminarResultado(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)


@app.route("/resultados/mesa/<string:id_mesa>", methods=['GET'])
def inscritosEnMesa(id_mesa):
    json = miControladorResultado.listarInscritosEnMesa(id_mesa)
    return jsonify(json)


@app.route("/resultados/votaciones_mayores", methods=['GET'])
def getVotacionesMayores(miControladorResultado):
    json = miControladorResultado.votacionesMasAltasPorpartido()
    return jsonify(json)


@app.route("/resultados/promedio_votaciones/mesa/<string:id_mesa>", methods=['GET'])
def getPromedioVotacionEnMesa(id_mesa):
    json = miControladorResultado.promedioVotacionEnMesa(id_mesa)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
