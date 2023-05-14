from Domain.undoRedoOperation import UndoRedoOperations


class UndoRedoService:
    def __init__(self):
        self.undoOperations = []
        self.redoOperations = []

    def adaugaOperatie(self, undoRedoOperation: UndoRedoOperations):
        self.undoOperations.append(undoRedoOperation)
        self.redoOperations.clear()

    def undo(self):
        if self.undoOperations:
            lUOperation = self.undoOperations.pop()
            self.redoOperations.append(lUOperation)
            lUOperation.doUndo()

    def redo(self):
        if self.redoOperations:
            lROperation = self.redoOperations.pop()
            self.undoOperations.append(lROperation)
            lROperation.doRedo()
