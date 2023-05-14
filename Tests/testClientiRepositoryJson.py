from Domain.cardClient import Client
from Repository.repositoryJson import RepositoryJson
from utils import clear_file


def testClientiRepositoryJson():
    filename = 'testClient.json'
    clear_file(filename)
    clientRepositoryJson = RepositoryJson(filename)

    add = Client('1', 'Prigoana', 'Clau', '8593865783214',
                 '16.01.2003', '18.09.2021')
    clientRepositoryJson.adauga(add)
    assert clientRepositoryJson.read(add.idEntitate) == add


def testStergeClientRepositoryJson():
    filename = "testClient.json"
    clear_file(filename)
    clientRepositoryJson = RepositoryJson(filename)

    add = Client('1', 'Prigoana', 'Clau', '8593865783214',
                 '16.01.2003', '18.09.2021')
    clientRepositoryJson.adauga(add)
    assert clientRepositoryJson.read(add.idEntitate) == add

    add = Client('2', 'Prigoana', 'Claudiu', '4444865783214',
                 '17.01.2002', '18.08.2021')
    clientRepositoryJson.adauga(add)
    assert clientRepositoryJson.read(add.idEntitate) == add

    deleted = "1"
    clientRepositoryJson.sterge(deleted)


def testModificaClientRepositoryJson():
    filename = "testClient.json"
    clear_file(filename)
    clientRepositoryJson = RepositoryJson(filename)

    add = Client('1', 'Prigoana', 'Clau', '8593865783214',
                 '16.01.2003', '18.09.2021')
    clientRepositoryJson.adauga(add)
    assert clientRepositoryJson.read(add.idEntitate) == add

    modify = Client('1', 'Maier', 'Andrei', '3333865783214',
                    '16.01.2003', '18.09.2021')

    clientRepositoryJson.modifica(modify)
    assert clientRepositoryJson.read(modify.idEntitate) == modify
