from Domain import tranzactie


class TranzactieValidator:
    def valideaza(self, tran: tranzactie):
        data1 = tran.data.split('.')
        if len(data1) != 3:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data1[0]) < 1 or int(data1[0]) > 31:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data1[1]) < 1 or int(data1[1]) > 12:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data1[2]) < 1900 or int(data1[2]) > 2021:
            raise KeyError("Data nu a fost introdusa corect!")

        ora = tran.ore.split(':')
        if len(ora) != 2:
            raise KeyError("Ora nu a fost introdusa corect!")
        if int(ora[0]) < 1 or int(ora[0]) > 24:
            raise KeyError("Ora nu a fost introdusa corect!")
        if int(ora[1]) < 0 or int(ora[1]) > 59:
            raise KeyError("Ora nu a fost introdusa corect!")
