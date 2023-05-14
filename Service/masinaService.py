from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Domain.operatiaAdauga import OperatiaAdauga
from Domain.operatiaModifica import OperatiaModifica
from Domain.operatiaMultipleActulizare import OperatiaMultiplaActulizare
from Domain.operatiaSterge import OperatiaSterge
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class MasinaService:
    def __init__(self, masinaRepository: Repository,
                 masinaValidator: MasinaValidator,
                 undoRedoService: UndoRedoService):
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__masinaRepository.read()

    def adauga(self, idMasina, model, anAchizitie,
               nrKm, inGarantie):
        '''
        adauga o noua masina in clasa
        :param idMasina: str
        :param model: str
        :param anAchizitie: int
        :param nrKm: int
        :param inGarantie: str
        '''
        masina = Masina(idMasina, model,
                        anAchizitie, nrKm, inGarantie)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.adauga(masina)
        self.__undoRedoService.adaugaOperatie(
            OperatiaAdauga(self.__masinaRepository, masina))

    def sterge(self, idMasina):
        '''sterge o masina duap un id dat'''
        masina = self.__masinaRepository.read(idMasina)
        self.__masinaRepository.sterge(idMasina)
        self.__undoRedoService.adaugaOperatie(
            OperatiaSterge(self.__masinaRepository, masina))

    def modifica(self, idMasina, model, anAchizite,
                 nrKm, inGarantie):
        '''modifica datele unei masini'''
        masinaVeche = self.__masinaRepository.read(idMasina)
        masina = Masina(idMasina, model, anAchizite,
                        nrKm, inGarantie)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.modifica(masina)
        self.__undoRedoService.adaugaOperatie(
            OperatiaModifica(self.__masinaRepository, masinaVeche, masina))

    def cautareFullText(self, para):
        masini = self.__masinaRepository.read()
        rez = []
        for i in masini:
            if para in i.model or para in str(i.anAchizitie) \
                    or para in str(i.nrKm) \
                    or para in ("da" if i.inGarantie else "nu"):
                rez.append(i)
        return rez

    def ActualizareGarantie(self):
        listaOVechi = []
        listaONou = []
        for masina in self.getAll():
            if int(masina.anAchizitie) >= 2018 and int(masina.nrKm) <= 60000:
                listaOVechi.append(masina)
                self.modifica(masina.idEntitate,
                              masina.model,
                              masina.anAchizitie,
                              masina.nrKm, 'da')
                listaONou.append(masina)
            else:
                listaOVechi.append(masina)
                self.modifica(masina.idEntitate,
                              masina.model,
                              masina.anAchizitie,
                              masina.nrKm, 'nu')
                listaONou.append(masina)
        self.__undoRedoService.adaugaOperatie(
            OperatiaMultiplaActulizare(self.__masinaRepository,
                                       listaOVechi, listaONou))
