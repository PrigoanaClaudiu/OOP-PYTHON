from Domain.entitate import Entitate
from Domain.undoRedoOperation import UndoRedoOperations
from Repository.repository import Repository


class OperatiaModifica(UndoRedoOperations):
    def __init__(self, repository: Repository,
                 oVechi: Entitate, oNou: Entitate):
        self.__repository = repository
        self.__oVechi = oVechi
        self.__oNou = oNou

    def doUndo(self):
        self.__repository.modifica(self.__oVechi)

    def doRedo(self):
        self.__repository.modifica(self.__oNou)
