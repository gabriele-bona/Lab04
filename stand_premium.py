from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    def prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = f"Assegnato a {self.espositore.codice}"
        return f"Stand n.{self.codice} di {self.superficie} m^2 localizzato in area {self.__posizione} al padiglione {self.padiglione} | costo: {self.prezzo():.2f} euro | {stato}"