from Domain.masina import Masina
from Repository.repositoryJson import RepositoryJson
from Service import masinaService
from Service.masinaService import MasinaService
from utils import clear_file


def testMasiniRepositoryJson():
    filename = 'testMasini.json'
    clear_file(filename)
    masinaRepositoryJson = RepositoryJson(filename)

    add = Masina('1', 'Dacia', 2003, 100, 'da')
    masinaRepositoryJson.adauga(add)
    assert masinaRepositoryJson.read(add.idEntitate) == add


def testStergeMasinaRepositoryJson():
    filename = 'testMasini.json'
    clear_file(filename)
    masinaRepositoryJson = RepositoryJson(filename)

    add = Masina('1', 'Dacia', 2003, 100, 'da')
    masinaRepositoryJson.adauga(add)
    assert masinaRepositoryJson.read(add.idEntitate) == add

    add = Masina('2', 'BMW', 2010, 200, 'da')
    masinaRepositoryJson.adauga(add)
    assert masinaRepositoryJson.read(add.idEntitate) == add

    deleted = '1'
    masinaRepositoryJson.sterge(deleted)


def testModificaMasinaRepositoryJson():
    filename = 'testMasini.json'
    clear_file(filename)
    masinaRepositoryJson = RepositoryJson(filename)

    add = Masina('1', 'Dacia', 2003, 100, 'da')
    masinaRepositoryJson.adauga(add)
    assert masinaRepositoryJson.read(add.idEntitate) == add

    modify = Masina('1', 'Logan', 2009, 200, 'da')
    masinaRepositoryJson.modifica(modify)
    assert masinaRepositoryJson.read(modify.idEntitate) == modify
