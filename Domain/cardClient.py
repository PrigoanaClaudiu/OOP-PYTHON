from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Client(Entitate):
    '''
    Creeaza un client
    id -> trebuie sa fie unic
    cnp -> trebuie sa fie unic
    '''
    nume: str
    prenume: str
    CNP: str
    dataN: str
    dataI: str
