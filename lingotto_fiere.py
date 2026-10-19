from stand import Stand
from espositore import Espositore
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.stand = {}
        self.espositori = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for riga in file:
                    riga = riga.strip()
                    if not riga:
                        continue
                    lista_riga = riga.split(',')
                    codice = lista_riga[0].strip()
                    if codice[0:2] == 'ST':
                        superficie = float(lista_riga[1].strip())
                        padiglione = int(lista_riga[2].strip())
                        prezzo_base = float(lista_riga[3].strip())
                        if len(lista_riga) == 4:
                            stand = Stand(codice, superficie, padiglione, prezzo_base)
                        elif len(lista_riga) == 5:
                            extra = lista_riga[4].strip()
                            if extra.isdigit():
                                stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, extra)
                            else:
                                stand = StandPremium(codice, superficie, padiglione, prezzo_base, extra)
                        else:
                            continue
                        self.stand[codice] = stand
                    elif codice[0:2] == 'ES':
                        nome = lista_riga[1].strip()
                        cognome = lista_riga[2].strip()
                        espositore = Espositore(codice, nome, cognome)
                        self.espositori[codice] = espositore
        except FileNotFoundError:
            raise FileNotFoundError(f"Errore: Il file {file_path} non è stato trovato.")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stand:
            raise ValueError(f"Lo stand {codice_stand} non esiste")
        if codice_espositore not in self.espositori:
            raise ValueError(f"L'espositore {codice_espositore} non esiste.")
        stand = self.stand[codice_stand]
        espositore = self.espositori[codice_espositore]
        if not stand.disponibile:
            raise ValueError(f"Lo stand {codice_stand} è già stato assegnato a un altro espositore.")
        for s in self.stand.values():
            if s.espositore == espositore:
                raise ValueError(f"L'espositore {codice_espositore} ha già uno stand assegnato.")
        stand.disponibile = False
        stand.espositore = espositore

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.espositori.values():
            stand_associato = None
            for stand in self.stand.values():
                if stand.espositore == espositore:
                    stand_associato = stand
                    break
            if stand_associato:
                print(f"{espositore} associato allo Stand: {stand_associato.codice} ({stand_associato.prezzo()}€)")
            else:
                print(f"{espositore} associato a nessuno stand")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand.values())