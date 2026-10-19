from stand import Stand

class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__numero_prese = int(numero_prese)

    @property
    def numero_prese(self):
        return self.__numero_prese

    def prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.__numero_prese)

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = f"Assegnato a {self.espositore.codice}"
        return f"Stand n.{self.codice} di {self.superficie} m^2 localizzato al padiglione {self.padiglione} | costo: {self.prezzo():.2f} euro con {self.__numero_prese} prese | {stato}"