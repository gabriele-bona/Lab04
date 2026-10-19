class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice(self):
        return self.__codice

    @property
    def nome(self):
        return self.__nome

    @property
    def cognome(self):
        return self.__cognome

    def __str__(self):
        return f"Espositore n.{self.__codice}: {self.__nome} {self.__cognome}"

    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self.__codice == other.__codice
        return False