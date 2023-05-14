from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Tranzactie(Entitate):
    '''
    id ->trebuie sa fie unic
    idMasina -> trebuie sa existe o masina cu id ul dat
    idCardClient -> trebuie sa existe un client cu id ul dat
    '''
    idMasina: str
    idClient: str
    sumaPiese: float
    sumaManopera: float
    data: str
    ore: str
