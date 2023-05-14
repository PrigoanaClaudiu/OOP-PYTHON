from typing import List

from Domain.undoRedoOperation import UndoRedoOperations
from Repository.repository import Repository


class OperataiaStergeCascada(UndoRedoOperations):
    def __init__(self, repository: Repository,
                 tranzactieRepository: Repository,
                 cascadaList: List):
        self.repository = repository
        self.tranzactieRepository = tranzactieRepository
        self.cascadaList = cascadaList

    def doUndo(self):
        for i in range(len(self.cascadaList) - 1):
            self.tranzactieRepository.adauga(self.cascadaList[i])
        self.repository.adauga(self.cascadaList[-1])

    def doRedo(self):
        for i in range(len(self.cascadaList) - 1):
            self.tranzactieRepository.sterge(self.cascadaList[i].idEntitate)
        self.repository.sterge(self.cascadaList[-1].idEntitate)
