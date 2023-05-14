from Domain import cardClient


class ClientValidator:
    def valideaza(self, client: cardClient):
        data = client.dataN.split('.')
        if len(data) != 3:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data[0]) < 1 or int(data[0]) > 31:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data[1]) < 1 or int(data[1]) > 12:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data[2]) < 1900 or int(data[2]) > 2021:
            raise KeyError("Data nu a fost introdusa corect!")

        data1 = client.dataI.split('.')
        if len(data1) != 3:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data1[0]) < 1 or int(data1[0]) > 31:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data1[1]) < 1 or int(data1[1]) > 12:
            raise KeyError("Data nu a fost introdusa corect!")
        if int(data1[2]) < 1900 or int(data1[2]) > 2021:
            raise KeyError("Data nu a fost introdusa corect!")
