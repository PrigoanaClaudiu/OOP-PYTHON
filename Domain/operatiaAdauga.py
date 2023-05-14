from Domain.entitate import Entitate
from Domain.undoRedoOperation import UndoRedoOperations
from Repository.repository import Repository


class OperatiaAdauga(UndoRedoOperations):
    def __init__(self, repository: Repository,
                 obiect: Entitate):
        self.reposotiry = repository
        self.obiect = obiect

    def doUndo(self):
        self.reposotiry.sterge(self.obiect.idEntitate)

    def doRedo(self):
        self.reposotiry.adauga(self.obiect)
