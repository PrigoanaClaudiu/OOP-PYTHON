from Domain.cardClient \
    import Client
from Domain.clientValidator \
    import ClientValidator
from Domain.masina \
    import Masina
from Domain.masinaValidator \
    import MasinaValidator
from Domain.tranzactie \
    import Tranzactie
from Domain.tranzactieValidator \
    import TranzactieValidator
from Repository.repositoryJson \
    import RepositoryJson
from Service.clientService \
    import ClientService
from Service.masinaService \
    import MasinaService
from Service.tranzactieService \
    import TranzactieService
from Service.undoRedoService \
    import UndoRedoService
from ViewModel.clientReduceriViewModel \
    import ClientReduceriViewModel
from utils import clear_file


def testCautareFullText():
    clear_file("testClient.json")
    clientRepository = RepositoryJson("testClient.json")
    clientValidator = ClientValidator()
    undoRedoService = UndoRedoService()
    clientService = \
        ClientService(clientRepository, clientValidator, undoRedoService)

    clientService.adauga('1', 'Prigoana', 'Clau', '8593865783214',
                         '16.01.2003', '18.09.2021')
    clientService.adauga('2', 'Prigoana', 'Claudiu', '4444865783214',
                         '17.01.2002', '18.08.2021')

    rez = clientService.cautareFullText('4444')
    assert rez == [Client(idEntitate='2', nume='Prigoana',
                          prenume='Claudiu', CNP='4444865783214',
                          dataN='17.01.2002', dataI='18.08.2021')]

    clear_file("testMasini.json")
    masinaRepository = \
        RepositoryJson("testMasini.json")
    masinaValidator = MasinaValidator()
    undoRedoService = UndoRedoService()
    masinaService = \
        MasinaService(masinaRepository, masinaValidator, undoRedoService)

    masinaService.adauga('1', 'dacia', 2019, 4000, 'nu')
    masinaService.adauga('2', 'logan', 2020, 60000, 'da')

    rez = masinaService.cautareFullText('ia')
    assert rez == [Masina(idEntitate='1', model='dacia',
                          anAchizitie=2019, nrKm=4000, inGarantie='nu')]


def testAfsTranzDinInterval():
    clear_file("testClient.json")
    clientRepository = RepositoryJson("testClient.json")
    clientValidator = ClientValidator()
    undoRedoService = UndoRedoService()
    clientService = \
        ClientService(clientRepository, clientValidator, undoRedoService)

    clientService.adauga('1', 'Prigoana', 'Clau', '8593865783214',
                         '16.01.2003', '18.09.2021')
    clientService.adauga('2', 'Prigoana', 'Claudiu', '4444865783214',
                         '17.01.2002', '18.08.2021')
    clear_file("testMasini.json")
    masinaRepository = RepositoryJson("testMasini.json")
    masinaValidator = MasinaValidator()
    undoRedoService = UndoRedoService()
    masinaService = \
        MasinaService(masinaRepository, masinaValidator, undoRedoService)

    masinaService.adauga('1', 'dacia', 2019, 4000, 'nu')
    masinaService.adauga('2', 'logan', 2020, 60000, 'da')

    clear_file('testTranzactii.json')
    tranzactieRepository = RepositoryJson("testTranzactii.json")
    tranzactieValidator = TranzactieValidator()
    undoRedoService = UndoRedoService()
    tranzactieService = TranzactieService(tranzactieRepository,
                                          tranzactieValidator,
                                          masinaRepository,
                                          masinaValidator,
                                          clientRepository,
                                          clientValidator,
                                          undoRedoService)

    tranzactieService. \
        adauga("1", "1", "1", 200, 300, "18.09.2019", "17:01")
    tranzactieService. \
        adauga("2", "2", "1", 300, 100, "16.02.2009", "19:10")

    a = 0
    b = 100
    tranzactii = tranzactieService.getAll()
    rez = []
    for i in tranzactii:
        if a <= i.sumaPiese + i.sumaManopera <= b:
            rez.append(i)

    assert rez == [Tranzactie(idEntitate='2',
                              idMasina='2',
                              idClient='1',
                              sumaPiese=0,
                              sumaManopera=90.0,
                              data='16.02.2009', ore='19:10')]


def testMasiniOrdonateDupaSumaPeManopera():
    clear_file("testClient.json")
    clientRepository = RepositoryJson("testClient.json")
    clientValidator = ClientValidator()
    undoRedoService = UndoRedoService()
    clientService = \
        ClientService(clientRepository, clientValidator, undoRedoService)

    clientService.adauga('1', 'Prigoana', 'Clau', '8593865783214',
                         '16.01.2003', '18.09.2021')
    clientService.adauga('2', 'Prigoana', 'Claudiu', '4444865783214',
                         '17.01.2002', '18.08.2021')
    clear_file("testMasini.json")
    masinaRepository = RepositoryJson("testMasini.json")
    masinaValidator = MasinaValidator()
    undoRedoService = UndoRedoService()
    masinaService = \
        MasinaService(masinaRepository, masinaValidator, undoRedoService)

    masinaService.adauga('1', 'dacia', 2019, 4000, 'nu')
    masinaService.adauga('2', 'logan', 2020, 60000, 'da')

    clear_file('testTranzactii.json')
    tranzactieRepository = RepositoryJson("testTranzactii.json")
    tranzactieValidator = TranzactieValidator()
    undoRedoService = UndoRedoService()
    tranzactieService = \
        TranzactieService(tranzactieRepository, tranzactieValidator,
                          masinaRepository, masinaValidator, clientRepository,
                          clientValidator, undoRedoService)

    tranzactieService. \
        adauga("1", "1", "1", 200, 300, "18.09.2019", "17:01")
    tranzactieService. \
        adauga("2", "2", "1", 300, 100, "16.02.2009", "19:10")

    rez = tranzactieService.afisareMasinilorOrdDescDupaManopera()

    assert rez[0] == {'masina': Masina(
        idEntitate='1', model='dacia',
        anAchizitie=2019, nrKm=4000, inGarantie='nu'), 'pretManopera': 270.0}
    assert rez[1] == {'masina': Masina(
        idEntitate='2', model='logan',
        anAchizitie=2020, nrKm=60000, inGarantie='da'), 'pretManopera': 90.0}


def testClientiOrdoDupaReducere():
    clear_file("testClient.json")
    clientRepository = RepositoryJson("testClient.json")
    clientValidator = ClientValidator()
    undoRedoService = UndoRedoService()
    clientService = \
        ClientService(clientRepository, clientValidator, undoRedoService)

    clientService.adauga('1', 'Prigoana', 'Clau', '8593865783214',
                         '16.01.2003', '18.09.2021')
    clientService.adauga('2', 'Prigoana', 'Claudiu', '4444865783214',
                         '17.01.2002', '18.08.2021')

    clear_file("testMasini.json")
    masinaRepository = RepositoryJson("testMasini.json")
    masinaValidator = MasinaValidator()
    undoRedoService = UndoRedoService()
    masinaService = \
        MasinaService(masinaRepository, masinaValidator, undoRedoService)

    masinaService.adauga('1', 'dacia', 2019, 4000, 'nu')
    masinaService.adauga('2', 'logan', 2020, 60000, 'da')

    clear_file('testTranzactii.json')
    tranzactieRepository = RepositoryJson("testTranzactii.json")
    tranzactieValidator = TranzactieValidator()
    undoRedoService = UndoRedoService()
    tranzactieService = \
        TranzactieService(tranzactieRepository, tranzactieValidator,
                          masinaRepository, masinaValidator, clientRepository,
                          clientValidator, undoRedoService)

    tranzactieService.adauga("1", "1", "1", 200, 300, "18.09.2019", "17:01")
    tranzactieService.adauga("2", "2", "1", 300, 100, "16.02.2009", "19:10")

    rez = tranzactieService.afisareCardClientOrdDupaRed()

    assert \
        ClientReduceriViewModel(str(rez[0].nume) == 'Prigoana',
                                str(rez[0].prenume) == 'Clau',
                                rez[0].reduceri == 36)
    assert \
        ClientReduceriViewModel(str(rez[1].nume) == 'Prigoana',
                                str(rez[1].prenume) == 'Claudiu',
                                rez[1].reduceri == 0)


def testStergereTranz():
    clear_file("testClient.json")
    clientRepository = RepositoryJson("testClient.json")
    clientValidator = ClientValidator()
    undoRedoService = UndoRedoService()
    clientService = \
        ClientService(clientRepository, clientValidator, undoRedoService)

    clientService.adauga('1', 'Prigoana', 'Clau', '8593865783214',
                         '16.01.2003', '18.09.2021')
    clientService.adauga('2', 'Prigoana', 'Claudiu', '4444865783214',
                         '17.01.2002', '18.08.2021')

    clear_file("testMasini.json")
    masinaRepository = RepositoryJson("testMasini.json")
    masinaValidator = MasinaValidator()
    undoRedoService = UndoRedoService()
    masinaService = \
        MasinaService(masinaRepository, masinaValidator, undoRedoService)

    masinaService.adauga('1', 'dacia', 2019, 4000, 'nu')
    masinaService.adauga('2', 'logan', 2020, 60000, 'da')

    clear_file('testTranzactii.json')
    tranzactieRepository = RepositoryJson("testTranzactii.json")
    tranzactieValidator = TranzactieValidator()
    undoRedoService = UndoRedoService()
    tranzactieService = \
        TranzactieService(tranzactieRepository, tranzactieValidator,
                          masinaRepository, masinaValidator, clientRepository,
                          clientValidator, undoRedoService)

    tranzactieService.adauga("1", "1", "1", 200, 300, "18.09.2019", "17:01")
    tranzactieService.adauga("2", "2", "1", 300, 100, "16.02.2009", "19:10")

    a1 = "15.09.2018"
    b1 = "26.12.2021"
    tranzactieService.StergereTranzDinIntervalDeZile(a1, b1)
    assert tranzactieService.getAll() \
           == [Tranzactie(idEntitate='2', idMasina='2',
                          idClient='1', sumaPiese=0,
                          sumaManopera=90.0, data='16.02.2009', ore='19:10')]

    tranzactieService.adauga("1", "1", "1", 200, 300, "18.09.2019", "17:01")
    a1 = "16.01.2008"
    b1 = "16.01.2015"
    tranzactieService. \
        StergereTranzDinIntervalDeZile(a1, b1)
    assert tranzactieService.getAll() \
           == [Tranzactie(idEntitate='1', idMasina='1',
                          idClient='1', sumaPiese=200,
                          sumaManopera=270.0,
                          data='18.09.2019', ore='17:01')]
