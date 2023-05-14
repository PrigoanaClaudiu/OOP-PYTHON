from Domain.entitate import Entitate
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, idEntitate=None):
        if idEntitate is None:
            return list(self.entitati.values())
        if idEntitate in self.entitati:
            return self.entitati[idEntitate]
        else:
            return None

    def adauga(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat.")
        self.entitati[entitate.idEntitate] = entitate

    def sterge(self, idEntitate):
        if self.read(idEntitate) is None:
            raise KeyError("Nu exista o astfel de entitate.")
        del self.entitati[idEntitate]

    def modifica(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is None:
            raise KeyError("Nu exista o astfel de entitate.")
        self.entitati[entitate.idEntitate] = entitate
