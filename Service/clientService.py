from random import randint, choice

from Domain.cardClient import Client
from Domain.clientValidator import ClientValidator
from Domain.operatiaAdauga import OperatiaAdauga
from Domain.operatiaModifica import OperatiaModifica
from Domain.operatiaSterge import OperatiaSterge
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class ClientService:
    def __init__(self, clientRepository: Repository,
                 clientValidator: ClientValidator,
                 undoRedoService: UndoRedoService):
        self.__clientRepository = clientRepository
        self.__clientValidator = clientValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        "afiseaza toti clientii"
        return self.__clientRepository.read()

    def adauga(self, idClient, nume, prenume,
               CNP, dataN, dataI):
        '''
        adauga un client nou
        :param idClient: str
        :param nume: str
        :param prenume: str
        :param CNP: str
        :param dataN: str
        :param dataI: str
        :return: clientul nou
        '''
        client = Client(idClient, nume, prenume,
                        CNP, dataN, dataI)
        self.__clientValidator.valideaza(client)
        self.__clientRepository.adauga(client)
        self.__undoRedoService.adaugaOperatie(
            OperatiaAdauga(self.__clientRepository, client))

    def sterge(self, idClient):
        '''
        sterge un anumit client
        :param idClient: id ul clientului ce trb sters
        :return: clasa dupa stergere
        '''
        client = self.__clientRepository.read(idClient)
        self.__clientRepository.sterge(idClient)
        self.__undoRedoService.adaugaOperatie(
            OperatiaSterge(self.__clientRepository, client))

    def modifica(self, idClient, nume, prenume, CNP, dataN, dataI):
        '''
        modifica datele unui anumit client
        :param idClient: id ul clientului str
        :param nume: numele nou
        :param prenume: prenumele nou
        :param CNP: cnp-ul nou
        :param dataN: data nasterii noi
        :param dataI: data inregistrarii noi
        :return: clasa cu datele clientului modificate
        '''
        clientVechi = self.__clientRepository.read(idClient)
        client = Client(idClient, nume, prenume,
                        CNP, dataN, dataI)
        self.__clientValidator.valideaza(client)
        self.__clientRepository.modifica(client)
        self.__undoRedoService.adaugaOperatie(
            OperatiaModifica(self.__clientRepository, clientVechi, client))

    def verifCNP(self, nume, prenume, CNP, dataN, dataI):
        if not all([nume, prenume, CNP, dataN, dataI]):
            raise IndexError
        if CNP in [client.CNP for client in self.__clientRepository.read()]:
            print("CNP-ul deja exista!")

    def cautareFullText(self, para):
        clienti = self.__clientRepository.read()
        rez = []
        for i in clienti:
            if para in i.nume or para in i.prenume \
                    or para in i.CNP or para in i.dataN \
                    or para in i.dataI:
                rez.append(i)
        return rez

    def clientiGenerati(self, n: int):
        '''
        generare n clienti random
        :param n: int
        :return: n clienti random cu date valide
        '''
        nrClienti = 0
        while True:
            idClient = str(randint(1, 100000))
            numeC = ['Pop', 'Prigoana', 'Marginean', 'Lupas', 'Pasca', 'Nemes']
            nume = choice(numeC)
            prenumeC = ['Claudiu', 'Alex', 'Adi', 'Razvan', 'Denis', 'Marius']
            prenume = choice(prenumeC)
            cnp = str(randint(1000000000000, 9999999999999))
            dataNas = ['16.01.2003', '17.01.1993', '20.08.1994', '09.08.1999']
            dataN = choice(dataNas)
            dataInr = ['18.01.2019', '19.09.2020', '21.09.2021', '23.08.2021']
            dataI = choice(dataInr)
            client = Client(idClient, nume, prenume, cnp, dataN, dataI)
            if self.__clientRepository.read(idClient) is None:
                nrClienti = nrClienti + 1
                self.__clientRepository.adauga(client)
                if nrClienti == n:
                    break
