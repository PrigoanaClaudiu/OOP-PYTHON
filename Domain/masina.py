from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Masina(Entitate):
    '''
    Creeaza o masina
    id -> este unic
    anAchiztie -> un nr pozitiv
    nrKm -> un nr pozitiv
    garantie -> da/nu
    '''
    model: str
    anAchizitie: int
    nrKm: int
    inGarantie: str
