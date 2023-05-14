from Domain.undoRedoOperation import UndoRedoOperations
from Repository.repository import Repository


class OperatiaMultiplaActulizare(UndoRedoOperations):
    def __init__(self, repository: Repository,
                 listaOVechi: list, listaONou: list):
        self.__repository = repository
        self.__listaOVechi = listaOVechi
        self.__listaONou = listaONou

    def doUndo(self):
        for entitate in self.__listaOVechi:
            self.__repository.modifica(entitate)

    def doRedo(self):
        for entitate in self.__listaONou:
            self.__repository.modifica(entitate)
