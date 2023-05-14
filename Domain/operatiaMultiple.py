from Domain.undoRedoOperation import UndoRedoOperations
from Repository.repository import Repository


class OperatiaMultipla(UndoRedoOperations):
    def __init__(self, repository: Repository,
                 obiecteSterse: list):
        self.repository = repository
        self.obiecteSterse = obiecteSterse

    def doUndo(self):
        for entitate in self.obiecteSterse:
            self.repository.adauga(entitate)

    def doRedo(self):
        for entitate in self.obiecteSterse:
            self.repository.sterge(entitate)
