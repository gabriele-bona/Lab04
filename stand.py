class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = (superficie)
        self.__padiglione = padiglione
        self.__prezzo_base = prezzo_base
        self.disponibile = True
        self.espositore = None

    @property
    def codice(self):
        return self.__codice

    @property
    def superficie(self):
        return self.__superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzo_base(self):
        return self.__prezzo_base

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = f"Assegnato a {self.espositore.codice}"
        return f"Stand n.{self.__codice} di {self.__superficie} m^2 localizzato al padiglione {self.__padiglione} | costo: {self.prezzo():.2f} euro | {stato}"

    def prezzo(self):
        return self.__prezzo_base

    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.prezzo() < other.prezzo()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.__codice == other.__codice
        return False