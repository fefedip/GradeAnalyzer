import csv
from esame import Esame
from pathlib import Path

class Analyzer:
    def __init__(self):
        self.lista_esami=[]
        try:
            percorso_csv= Path(__file__).parent / ".." / "data" / "voti.csv"
            with open(percorso_csv, "r") as f:
                lettore=csv.DictReader(f)
                for riga in lettore:
                    exam = Esame(riga["Esame"], int(riga["cfu"]), int(riga["voto"]))
                    self.lista_esami.append(exam)
        except FileNotFoundError:
            print("File not found. Please create a valid CSV file.")


    def calculate_weighted_average(self):
        cfu_tot=0
        pesi=0
        for exam in self.lista_esami:
            cfu_tot+=exam.cfu
            peso=exam.calculate_exam_weight()
            pesi+=peso
        return pesi/cfu_tot


    def calculate_average(self):
        i=0
        sum=0
        for exam in self.lista_esami:
            i+=1
            sum+=exam.voto
        return sum/i

    def estimate_vote_for_average(self, target, cfu):
        cfu_totali=0
        peso_tot=0
        voto = 0
        for exam in self.lista_esami:
            cfu_totali+=exam.cfu
            peso_tot+=exam.calculate_exam_weight()
        cfu_totali+=cfu
        voto = ((target*cfu_totali)-peso_tot) / cfu
        if (voto <= 30):
            return voto
        else:
            print("You can't reach that average with a valid grade!")