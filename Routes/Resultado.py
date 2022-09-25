from flask import Flask, jsonify, request, Blueprint
from Controladores.ControladorResultado import ControladorResultado

miControladorResultado=ControladorResultado()

resultado = Blueprint('resultado', __name__)

@resultado.route('/resultados', methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)


@resultado.route("/resultado",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=miControladorResultado.create(data)
    return jsonify(json)


@resultado.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)


@resultado.route("/resultado/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json=miControladorResultado.update(id,data)
    return jsonify(json)

@resultado.route("/reportes",methods=['GET'])
def totalVotos():
    json = miControladorResultado.cantidadTotalVotos()
    return jsonify(json)

@resultado.route("/reportes/<string:id>",methods=['GET'])
def totalVotosCandidato(id):
    json = miControladorResultado.cantidadVotosCandidato(id)
    return jsonify(json)

@resultado.route("/reportes/candidatos", methods=['GET'])
def totalVotosCandidatos():
    json = miControladorResultado.cantidadVotosCandidatos()
    return jsonify(json)

@resultado.route("/reportes/ganador", methods=['GET'])
def totalVotosGanador():
    json = miControladorResultado.candidatoGanador()
    return jsonify(json)