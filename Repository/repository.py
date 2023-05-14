from typing import Protocol

from Domain.entitate import Entitate


class Repository(Protocol):
    def read(self, idEntitate=None):
        ...

    def adauga(self, entitate: Entitate) -> None:
        ...

    def sterge(self, idEntitate) -> None:
        ...

    def modifica(self, entitate: Entitate) -> None:
        ...
