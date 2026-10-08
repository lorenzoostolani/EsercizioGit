class Studente:
    def __init__(self, nome, cognome, eta, citta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta

    def classificazione(self):
        if 14 <= self.eta <= 16:
            return "Biennio"
        if 17 <= self.eta <= 19:
            return "Triennio"
        return "Altro"

    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.eta} anni, residente a {self.citta}"