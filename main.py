from Domain.clientValidator import ClientValidator
from Domain.masinaValidator import MasinaValidator
from Domain.tranzactieValidator import TranzactieValidator
from Repository.repositoryJson import RepositoryJson
from Service.clientService import ClientService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService
from Tests.testClientiRepositoryJson import \
    testClientiRepositoryJson, \
    testStergeClientRepositoryJson, \
    testModificaClientRepositoryJson
from Tests.testMasinaRepositoryJson import \
    testMasiniRepositoryJson, \
    testStergeMasinaRepositoryJson, \
    testModificaMasinaRepositoryJson
from Tests.testTranzactieRepositoryJson import \
    testTranzactieRepositoryJson, \
    testModificaTranzactieRepositoryJson
from Tests.testeFunctionalitati import \
    testMasiniOrdonateDupaSumaPeManopera, \
    testClientiOrdoDupaReducere, \
    testCautareFullText, \
    testAfsTranzDinInterval, testStergereTranz
from UI.console import Console


def main():
    undoRedoService = UndoRedoService()

    masinaRepositoryJson = RepositoryJson("masini.json")
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepositoryJson,
                                  masinaValidator, undoRedoService)

    clientRepositoryJson = RepositoryJson("clienti.json")
    clientValidator = ClientValidator()
    clientService = ClientService(clientRepositoryJson,
                                  clientValidator, undoRedoService)

    tranzactieRepositoryJson = RepositoryJson("tranzactii.json")
    tranzactieValidator = TranzactieValidator()
    tranzactieService = TranzactieService(tranzactieRepositoryJson,
                                          tranzactieValidator,
                                          masinaRepositoryJson,
                                          masinaValidator,
                                          clientRepositoryJson,
                                          clientValidator,
                                          undoRedoService
                                          )
    consola = Console(masinaService, clientService,
                      tranzactieService, undoRedoService)
    consola.runMenu()


if __name__ == '__main__':
    testClientiRepositoryJson()
    testStergeClientRepositoryJson()
    testModificaClientRepositoryJson()
    testMasiniRepositoryJson()
    testStergeMasinaRepositoryJson()
    testModificaMasinaRepositoryJson()
    testTranzactieRepositoryJson()
    testModificaTranzactieRepositoryJson()
    testMasiniOrdonateDupaSumaPeManopera()
    testClientiOrdoDupaReducere()
    testCautareFullText()
    testAfsTranzDinInterval()
    testStergereTranz()
main()
