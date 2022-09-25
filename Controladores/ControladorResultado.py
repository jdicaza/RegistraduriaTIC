from sesiones.db import db
from Modelos.ModeloResultado import ModeloResultado
from Modelos.ModeloCandidato import ModeloCandidato
from Modelos.ModeloPartido import ModeloPartido
from Modelos.ModeloMesa import ModeloMesa
from sqlalchemy import func


class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        try:
            resultados = ModeloResultado.query.all()
            datos = []
            for i in resultados:
                datos.append(i.resultado())
            return datos
        except Exception as ex:
            return {'message': str(ex)}, 500

    def create(self, elResultado):
        try:
            idmesa = elResultado.get('idmesa')
            idcandidato = elResultado.get('idcandidato')
            resultado_create = ModeloResultado(idmesa, idcandidato)
            result_create = db.session.add(resultado_create)
            db.session.commit()
            if result_create != 1:
                return {'message': 'Resultado Registrado'}
            else:
                return {'message': 'Error al registrar'}, 500

        except Exception as ex:
            return {'message': str(ex)}, 500

    def show(self, id):
        print("Mostrando Resultado con id ", id)
        resultado_show = ModeloResultado.query.get(id)
        if resultado_show is not None:
            result_show = ModeloResultado.resultado(resultado_show)
            return result_show
        else:
            return {'message': 'no existe registro con id: ' + id}

    def update(self, id, elResultado):
        try:
            print("Actualizando Resultado con id ", id)
            resultadoupdate = ModeloResultado.query.get(id)
            resultadoupdate.idmesa = elResultado.get('idmesa')
            resultadoupdate.idcandidato = elResultado.get('idcandidato')
            db.session.add(resultadoupdate)
            db.session.commit()
            return {'message': 'Resultado con id: ' + id + ' ha sido Actualizado'}

        except Exception as ex:
            return {'message': 'Resultado con id: ' + id + ' no existe'}

    def cantidadTotalVotos(self):
        totalvotos = db.session.query(ModeloResultado).count()
        return {'Conteo Global de votos': totalvotos}

    def cantidadVotosCandidato(self, id):
        votoscandidato = db.session.query(ModeloResultado).filter_by(idcandidato=id).count()
        nombrecandidato = db.session.query(ModeloCandidato).get(id).nombre
        apellidocandidato = db.session.query(ModeloCandidato).get(id).apellido
        partidocandidato = db.session.query(ModeloCandidato).get(id).idpartido
        nombrepartido = db.session.query(ModeloPartido).get(partidocandidato).nombre
        return {'Candidato': nombrecandidato + ' ' + apellidocandidato,
                'Partido Político': nombrepartido,
                'Cantidad de votos': votoscandidato
                }

    def cantidadVotosCandidatos(self):
        totalvotoscandidatos = []
        candidatos = []
        resultado = db.session.query(ModeloCandidato).all()

        for candidato in resultado:
            candidatos.append(candidato.idcandidato)

        for i in candidatos:
            nombrecandidatos = db.session.query(ModeloCandidato).get(i).nombre
            apellidocandidatos = db.session.query(ModeloCandidato).get(i).apellido
            partidocandidatos = db.session.query(ModeloCandidato).get(i).idpartido
            votoscandidatos = db.session.query(ModeloResultado).filter_by(idcandidato=i).count()
            partidocandidatos = db.session.query(ModeloCandidato).get(i).idpartido
            nombrepartidos = db.session.query(ModeloPartido).get(partidocandidatos).nombre

            totalvotoscandidatos.append({'Candidato': nombrecandidatos + ' ' + apellidocandidatos,
                'Partido Político': nombrepartidos,
                'Cantidad de votos': votoscandidatos
                })
        return totalvotoscandidatos

    def candidatoGanador(self):
        totalvotoscandidatos = []
        candidatos = []
        ganadorcandidato = []
        resultado = db.session.query(ModeloCandidato).all()

        for candidato in resultado:
            candidatos.append(candidato.idcandidato)

        for i in candidatos:
            ganadorcandidato.append(db.session.query(ModeloResultado).filter_by(idcandidato=i).count())
            votos_max = max(ganadorcandidato)
            votoscandidatos = db.session.query(ModeloResultado).filter_by(idcandidato=i).count()

        for i in candidatos:
            ganador_max = db.session.query(ModeloResultado).filter_by(idcandidato=i).count()
            if votos_max == ganador_max:
                nombrecandidato = db.session.query(ModeloCandidato).get(i).nombre
                apellidocandidato = db.session.query(ModeloCandidato).get(i).apellido
                partidocandidato = db.session.query(ModeloCandidato).get(i).idpartido
                nombrepartido = db.session.query(ModeloPartido).get(partidocandidato).nombre
                return {'Candidato': nombrecandidato + ' ' + apellidocandidato,
                        'Partido Político': nombrepartido,
                        'Cantidad de votos': votos_max
                        }
        print(ganadorcandidato)
        print(votos_max)




