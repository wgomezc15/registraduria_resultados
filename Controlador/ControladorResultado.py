from Modelo.Resultado import Resultado
from Modelo.Candidato import Candidato
from Modelo.Mesa import Mesa
from Repositorio.RepositorioResultado import RepositorioResultado
from Repositorio.RepositorioCandidato import RepositorioCandidato
from Repositorio.RepositorioMesa import RepositorioMesa
class ControladorResultado():

    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion candidato y mesa a resultado
    """
    def create(self,infoResultado,id_candidato,id_mesa):
        nuevoResultado=Resultado(infoResultado)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato=elCandidato
        nuevoResultado.mesa=laMesa
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de resultado (candidato y mesa)
    """
    def update(self,id,infoResultado,id_candidato,id_mesa):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.año=infoResultado["año"]
        elResultado.numero_mesa = infoResultado["numero_mesa"]
        elResultado.id_partido=infoResultado["id_partido"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)
    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener todos los inscritos en una mesa"
    def listarInscritosEnMesa(self,id_mesa):
        return self.repositorioResultado.getListadoInscritosEnMesa(id_mesa)
    "Obtener votaciones mas altas por partido"
    def votacionesMasAltasPorPartido(self):
        return self.repositorioResultado.getMayorVotacionPorPartido()

    "Obtener promedio de votaciones en mesa"
    def promedioVotacionesEnMesa(self,id_mesa):
        return self.repositorioResultado.promedioVotacionesEnMesa(id_mesa)