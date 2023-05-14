from Domain.clientValidator import ClientValidator
from Domain.masinaValidator import MasinaValidator
from Domain.operatiaAdauga import OperatiaAdauga
from Domain.operatiaModifica import OperatiaModifica
from Domain.operatiaMultiple import OperatiaMultipla
from Domain.operatiaSterge import OperatiaSterge
from Domain.operatiaStergeCascada import OperataiaStergeCascada
from Domain.tranzactie import Tranzactie
from Domain.tranzactieValidator import TranzactieValidator
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService
from ViewModel.clientReduceriViewModel import ClientReduceriViewModel


class TranzactieService:
    def __init__(self, tranzactieRepository: Repository,
                 tranzactieValidator: TranzactieValidator,
                 masinaRepository: Repository,
                 masinaValidator: MasinaValidator,
                 clientRepository: Repository,
                 clientValidator: ClientValidator,
                 undoRedoService: UndoRedoService):
        self.__tranzactieRepository = tranzactieRepository
        self.__tranzactieValidator = tranzactieValidator
        self.__clientRepository = clientRepository
        self.__clientValidator = clientValidator
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__tranzactieRepository.read()

    def adauga(self, id, idMasina, idClient,
               sumaPiese, sumaManopera, data, ore):
        if self.__masinaRepository.read(idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat.")
        if self.__clientRepository.read(idClient) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat.")
        tranzactie = Tranzactie(id, idMasina, idClient, sumaPiese,
                                sumaManopera, data, ore)
        self.__tranzactieValidator.valideaza(tranzactie)
        masina = self.__masinaRepository.read(idMasina)
        if self.__masinaValidator.garan(masina) is True:
            tranzactie.sumaPiese = 0
        if idClient is not None:
            self.__clientRepository.read(idClient)
            tranzactie.sumaManopera = \
                tranzactie.sumaManopera - 10 / 100 * tranzactie.sumaManopera
        self.__tranzactieRepository.adauga(tranzactie)
        self.__undoRedoService.adaugaOperatie(
            OperatiaAdauga(self.__tranzactieRepository, tranzactie))

    def sterge(self, id):
        tranzactie = self.__tranzactieRepository.read(id)
        self.__tranzactieRepository.sterge(id)
        self.__undoRedoService.adaugaOperatie(
            OperatiaSterge(self.__tranzactieRepository, tranzactie))

    def modifica(self, id, idMasina, idClient, sumaPiese,
                 sumaManopera, data, ore):
        if self.__masinaRepository.read(idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat.")
        if self.__clientRepository.read(idClient) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat.")
        tranzactieVeche = self.__tranzactieRepository.read(id)
        tranzactie = Tranzactie(id, idMasina, idClient, sumaPiese,
                                sumaManopera, data, ore)
        self.__tranzactieValidator.valideaza(tranzactie)
        masina = self.__masinaRepository.read(idMasina)
        if self.__masinaValidator.garan(masina) is True:
            tranzactie.sumaPiese = 0
        if idClient is not None:
            self.__clientRepository.read(idClient)
            tranzactie.sumaManopera = \
                tranzactie.sumaManopera - 10 / 100 * tranzactie.sumaManopera
        self.__tranzactieRepository.modifica(tranzactie)
        self.__undoRedoService.adaugaOperatie(
            OperatiaModifica(self.__tranzactieRepository,
                             tranzactieVeche, tranzactie))

    def StergereTranzDinIntervalDeZile(self, a1, b1):
        a = a1.split('.')
        b = b1.split('.')
        lista = []
        tranzactii = self.getAll()
        for tranzactie in tranzactii:
            tran = tranzactie.data.split('.')
            if a[2] < tran[2] < b[2]:
                self.sterge(tranzactie.idEntitate)
                lista.append(tranzactie)
            elif a[2] == tran[2] == b[2] \
                    and a[1] < tran[1] < b[1]:
                self.sterge(tranzactie.idEntitate)
                lista.append(tranzactie)
            elif a[2] == tran[2] == b[2] \
                    and a[1] == tran[1] == b[1] \
                    and a[0] < tran[0] < b[0]:
                self.sterge(tranzactie.idEntitate)
                lista.append(tranzactie)
        self.__undoRedoService.adaugaOperatie(
            OperatiaMultipla(self.__tranzactieRepository, lista))

    def afisareMasinilorOrdDescDupaManopera(self):
        rez = []
        pretManopera = {}
        for masina in self.__masinaRepository.read():
            pretManopera[masina.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            pretManopera[tranzactie.idMasina].append(tranzactie.sumaManopera)
        for idMasina in pretManopera:
            rez.append(
                {
                    "masina": self.__masinaRepository.read(idMasina),
                    "pretManopera": sum(pretManopera[idMasina])
                }
            )
        return sorted(rez, key=lambda mano: mano["pretManopera"], reverse=True)

    def afisareCardClientOrdDupaRed(self):
        rez = []
        clienti = self.__clientRepository.read()
        for client in clienti:
            tranClienti = filter(lambda tranzactie:
                                 tranzactie.idClient == client
                                 .idEntitate,
                                 self.getAll())
            suma = sum(tranzactie.sumaManopera for tranzactie
                       in tranClienti)
            reduceri = 10 / 100 * suma
            rez.append(ClientReduceriViewModel(client.nume,
                                               client.prenume,
                                               reduceri))
        return sorted(rez, key=lambda x: x.reduceri, reverse=True)

    def delCascada(self, idu):
        cascada = []

        for tranzactie in self.__tranzactieRepository.read():
            if tranzactie.idMasina == idu:
                cascada.append(tranzactie)
                self.__tranzactieRepository.sterge(tranzactie.idEntitate)

        masina = self.__masinaRepository.read(idu)
        cascada.append(masina)
        self.__masinaRepository.sterge(masina.idEntitate)

        self.__undoRedoService.adaugaOperatie(
            OperataiaStergeCascada(
                self.__masinaRepository,
                self.__tranzactieRepository, cascada))
