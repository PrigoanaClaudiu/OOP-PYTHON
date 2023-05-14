from Domain.tranzactie import Tranzactie
from Repository.repositoryJson import RepositoryJson
from utils import clear_file


def testTranzactieRepositoryJson():
    filename = 'testClient.json'
    clear_file(filename)
    tranzactieRepositoryJson = RepositoryJson(filename)

    add = Tranzactie('1', '1', '1', 200,
                     300, '18.09.2021', '19:20')
    tranzactieRepositoryJson.adauga(add)
    assert tranzactieRepositoryJson.read(add.idEntitate) == add


def testStergeTranzactieRepositoryJson():
    filename = 'testClient.json'
    clear_file(filename)
    tranzactieRepositoryJson = RepositoryJson(filename)

    add = Tranzactie('1', '1', '1', 200,
                     300, '18.09.2021', '19:20')
    tranzactieRepositoryJson.adauga(add)
    assert tranzactieRepositoryJson.read(add.idEntitate) == add

    add = Tranzactie('2', '1', '1', 200,
                     400, '18.09.2020', '16:20')
    tranzactieRepositoryJson.adauga(add)
    assert tranzactieRepositoryJson.read(add.idEntitate) == add

    deleted = "1"
    tranzactieRepositoryJson.sterge(deleted)


def testModificaTranzactieRepositoryJson():
    filename = 'testClient.json'
    clear_file(filename)
    tranzactieRepositoryJson = RepositoryJson(filename)

    add = Tranzactie('1', '1', '1', 200,
                     300, '18.09.2021', '19:20')
    tranzactieRepositoryJson.adauga(add)
    assert tranzactieRepositoryJson.read(add.idEntitate) == add

    modify = Tranzactie('1', '1', '1', 300, 200,
                        '19.20.2020', '20:30')
    tranzactieRepositoryJson.modifica(modify)
    assert tranzactieRepositoryJson.read(modify.idEntitate) == modify
