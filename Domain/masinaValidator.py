from Domain import masina
from Domain.masina import Masina


class MasinaValidator:
    def valideaza(self, masinuta: Masina):
        '''verifica daca numarul de km si anul achizitiei sunt pozitive'''
        erori = []
        if int(masinuta.anAchizitie) < 0:
            erori.append("Anul achizitiei trebuie sa fie mai mare ca 0.")
        if int(masinuta.nrKm) < 0:
            erori.append(("Nr de kilometrii trebuie sa fie mai mari ca 0."))
        m = ['da', 'nu']
        if masinuta.inGarantie not in m:
            erori.append("Garantie poate lua valorile da/nu.")
        if len(erori) > 0:
            raise ValueError(erori)

    def garan(self, masinuta: Masina):
        '''verifica daca masina este sau nu in garantie'''
        m = ['da', 'nu']
        if masinuta.inGarantie in m:
            if masinuta.inGarantie == 'da':
                return True
        return False
