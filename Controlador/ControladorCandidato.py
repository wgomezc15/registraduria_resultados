from Modelo.Candidato import Candidato

class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        print("Listar todos los candidatos")
        unCandidato={
        "_id":"abc123",
        "cedula":"123",
        "nombre":"Juan",
        "apellido":"Perez"
        }
        return [unCandidato]

    def create(self,infoCandidato):
        print("Crear un candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self,id):
        print("Mostrando un candidato con id ",id)
        elCandidato = {
        "_id": id,
        "cedula": "123",
        "nombre": "Juan",
        "apellido": "Perez"
        }
        return elCandidato

    def update(self,id,infoCandidato):
        print("Actualizando candidato con id ",id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self,id):
        print("Elimiando candidato con id ",id)
        return {"deleted_count":1}