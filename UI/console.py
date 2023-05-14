from Domain.operatiaMultiple import OperatiaMultipla
from Service.clientService import ClientService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService


class Console:
    def __init__(self, masinaService: MasinaService,
                 clientService: ClientService,
                 tranzactieService: TranzactieService,
                 undoRedoService: UndoRedoService):
        self.__masinaService = masinaService
        self.__clientService = clientService
        self.__tranzactieService = tranzactieService
        self.__undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1. CRUD masini.")
            print("2. CURD card client.")
            print("3. Crud tranzactii.")
            print("4. Functionalitati.")
            print("5. Generare random a clientilor.")
            print("6. Stergere in cascada.")
            print("u. Undo.")
            print("r. Redo.")
            print("x. Iesire.")
            optiune = input("Dati optiunea: ")

            if optiune == '1':
                self.runCRUDMasiniMenu()
            elif optiune == '2':
                self.runCRUDCardClientMenu()
            elif optiune == '3':
                self.runCRUDTranzactieMenu()
            elif optiune == '4':
                self.runFunctionalitati()
            elif optiune == '5':
                self.rand()
            elif optiune == '6':
                idu = input("Dati id-ul masinii ce trebuie sterse:")
                self.__tranzactieService.delCascada(idu)
            elif optiune == 'u':
                self.__undoRedoService.undo()
            elif optiune == 'r':
                self.__undoRedoService.redo()
            elif optiune == 'x':
                break
            else:
                print("Optiune invalida!REincarcati: ")

    def runCRUDMasiniMenu(self):
        while True:
            print("1. Adauga.")
            print("2. Sterge.")
            print("3. Modifica.")
            print("a. Afiseaza masinile.")
            print("x. Iesire.")
            optiune = input("Dati optiunea: ")

            if optiune == '1':
                self.uiAdaugaMasina()
            elif optiune == '2':
                self.uiStergeMasina()
            elif optiune == '3':
                self.uiModificaMasina()
            elif optiune == 'a':
                self.showAllMasini()
            elif optiune == 'x':
                break
            else:
                print("Optiune gresita, reincercati!")

    def uiAdaugaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii: ")
            model = input("Dati modelul: ")
            anAchizitie = input("Dati anul achizitiei: ")
            nrKm = input("Dati nr de kilometrii: ")
            inGarantie = input("Garantie? (da/nu): ")
            self.__masinaService.adauga(idMasina,
                                        model,
                                        anAchizitie,
                                        nrKm,
                                        inGarantie)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def uiStergeMasina(self):
        try:
            idMasina = input("Dati id-ul masinii ce "
                             "trebuie sterse: ")
            self.__masinaService.sterge(idMasina)
        except KeyError as e:
            print(e)

    def uiModificaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii ce"
                             "trebuie modificate: ")
            model = input("Dati modelul nou: ")
            anAchizitie = input("Dati anul achizitiei: ")
            nrKm = input("Dati noul nr de kilometrii: ")
            garantie = input("Este in garantie?(da sau nu) : ")
            self.__masinaService.modifica(idMasina,
                                          model,
                                          anAchizitie,
                                          nrKm,
                                          garantie)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showAllMasini(self):
        for masina in self.__masinaService.getAll():
            print(masina)

    def runCRUDCardClientMenu(self):
        while True:
            print("1. Adauga.")
            print("2. Sterge.")
            print("3. Modifica.")
            print("a. Afiseaza clienti.")
            print("x. Iesire.")
            optiune = input("Dati optiunea: ")

            if optiune == '1':
                self.uiAdaugaClient()
            elif optiune == '2':
                self.uiStergeClient()
            elif optiune == '3':
                self.uiModificaClient()
            elif optiune == 'a':
                self.showAllClient()
            elif optiune == 'x':
                break
            else:
                print("Optiune gresita, reincercati!")

    def uiAdaugaClient(self):
        try:
            idClient = input("Dati id-ul: ")
            nume = input("Dati numele: ")
            prenume = input("Dati prenumele: ")
            CNP = input("Dati CNP-ul: ")
            dataN = input("Dati data nasterii: ")
            dataI = input("Dati data inregistrarii: ")
            self.__clientService.verifCNP(nume, prenume,
                                          CNP, dataN, dataI)
            self.__clientService.adauga(idClient, nume,
                                        prenume, CNP,
                                        dataN, dataI)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def uiStergeClient(self):
        try:
            idClient = input("Dati id-ul clientului: ")
            self.__clientService.sterge(idClient)
        except KeyError as e:
            print(e)

    def uiModificaClient(self):
        try:
            idClient = input("Dati id-ul clientului: ")
            nume = input("Dati numele: ")
            prenume = input("Dati prenumele: ")
            CNP = input("Dati CNP-ul: ")
            dataN = input("Dati data nasterii: ")
            dataI = input("Dati data inregistrarii: ")
            self.__clientService.verifCNP(nume, prenume,
                                          CNP, dataN, dataI)
            self.__clientService.modifica(idClient, nume, prenume,
                                          CNP, dataN, dataI)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showAllClient(self):
        for client in self.__clientService.getAll():
            print(client)

    def runCRUDTranzactieMenu(self):
        while True:
            print("1. Adauga.")
            print("2. Sterge.")
            print("3. Modifica.")
            print("a. Afiseaza tranzactiile.")
            print("x. Iesire.")
            optiune = input("Dati optiunea: ")

            if optiune == '1':
                self.uiAdaugaTranzactie()
            elif optiune == '2':
                self.uiStergeTranzactie()
            elif optiune == '3':
                self.uiModificaTranzactie()
            elif optiune == 'a':
                self.showAllTranzactie()
            elif optiune == 'x':
                break
            else:
                print("Optiune gresita, reincercati!")

    def uiAdaugaTranzactie(self):
        try:
            id = input("Dati id-ul tranzactiei: ")
            idMasina = input("Dati id-ul masinii: ")
            idClient = input("Dati id-ul clientului: ")
            sumaPiese = float(input("Dati suma pieselor: "))
            sumaManopera = float(input("Dati suma manoperei: "))
            data = input("Dati data: ")
            ore = input("Dati ora: ")
            self.__tranzactieService.adauga(id, idMasina,
                                            idClient, sumaPiese,
                                            sumaManopera, data, ore)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def uiStergeTranzactie(self):
        try:
            id = input("Dati id-ul tranzactiei: ")
            self.__tranzactieService.sterge(id)
        except KeyError as e:
            print(e)
        except Exception as e:
            print(e)

    def uiModificaTranzactie(self):
        try:
            id = input("Dati id-ul tranzactiei ce trebuie modificate: ")
            idMasina = input("Dati id-ul masinii: ")
            idClient = input("Dati id-ul clientului: ")
            sumaPiese = float(input("Dati suma pieselor: "))
            sumaManopera = float(input("Dati suma manoperei: "))
            data = input("Dati data: ")
            ore = input("Dati ora: ")
            self.__tranzactieService.modifica(id, idMasina,
                                              idClient, sumaPiese,
                                              sumaManopera, data, ore)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def showAllTranzactie(self):
        rez = []
        for tranzactie in self.__tranzactieService.getAll():
            s = tranzactie.sumaManopera + tranzactie.sumaPiese
            rez.append({
                "tranzactia": tranzactie,
                "pretul total": s,
            })
        print(rez)

    def runFunctionalitati(self):
        while True:
            print("1. Cautare full text masini: ")
            print("2. Cautare full text clienti: ")
            print("3. Afisarea tuturor tranzactiilor cu suma cuprinsa "
                  "intr-un interval dat.")
            print("4. Afișarea mașinilor ordonate descrescător după "
                  "suma obținută pe manoperă.")
            print("5. Afișarea cardurilor client ordonate descrescător "
                  "după valoarea reducerilor obținute.")
            print("6. Ștergerea tuturor tranzacțiilor dintr-un anumit "
                  "interval de zile.")
            print("7. Actualizarea garanției la fiecare mașină: "
                  "o mașină este în garanție dacă și numai dacă "
                  "are maxim 3 ani de la achiziție "
                  "și maxim 60 000 de km.")
            print("x. Iesire.")

            optiune = input("Dati optiunea: ")
            if optiune == "1":
                para = input("Dati parametrul: ")
                self.uiCautareFullTextMasini(para)
            elif optiune == "2":
                para = input("Dati parametrul: ")
                self.uiCautareFullTextClienti(para)
            elif optiune == "3":
                a = float(input("Dati nr. mai mic al intervalului: "))
                b = float(input("Dati nr. mai mare al intervalului: "))
                self.uiAfisareTranzactiiCuSumaIntre(a, b)
            elif optiune == "4":
                self.uiAfisareaMasinilorOrdDescDupaManopera()
            elif optiune == "5":
                self.uiAfisareCardClientOrdDescDupaRed()
            elif optiune == "6":
                a1 = str(input("Dati prima data(dd.mm.yyyy): "))
                b1 = str(input("Dati a doua data(dd.mm.yyyy): "))
                self.__tranzactieService.StergereTranzDinIntervalDeZile(a1, b1)
            elif optiune == "7":
                self.__masinaService.ActualizareGarantie()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida. Reincearca: ")

    def uiCautareFullTextMasini(self, para):
        for i in self.__masinaService.cautareFullText(para):
            print(i)

    def uiCautareFullTextClienti(self, para):
        for i in self.__clientService.cautareFullText(para):
            print(i)

    def rand(self):
        while True:
            print("1. Genereaza n clienti random.")
            print("x. Iesire.")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                n = int(input("Dati numarul de clienti"
                              "pe care doriti sa ii generati: "))
                self.__clientService.clientiGenerati(n)
                self.showAllClient()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida. Reincercati.")

    def uiAfisareTranzactiiCuSumaIntre(self, a, b):
        tranzactii = self.__tranzactieService.getAll()
        rez = []
        for i in tranzactii:
            if a <= i.sumaPiese + i.sumaManopera <= b:
                rez.append(i)
        print(rez)

    def uiAfisareaMasinilorOrdDescDupaManopera(self):
        for masina in \
                self.__tranzactieService.afisareMasinilorOrdDescDupaManopera():
            print(masina)

    def uiAfisareCardClientOrdDescDupaRed(self):
        for client in self.__tranzactieService.afisareCardClientOrdDupaRed():
            print(client)
