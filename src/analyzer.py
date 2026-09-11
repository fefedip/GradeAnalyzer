import csv
from esame import Esame

class Analyzer:
    def __init__(self):
        self.lista_esami=[]
        with open("/home/federico/Python/grade-analyzer/data/voti.csv", "r") as f:
            lettore=csv.DictReader(f)
            for riga in lettore:
                exam = Esame(riga["esame"], int(riga["cfu"]), int(riga["voto"]))
                self.lista_esami.append(exam)



    def calculate_weighted_average(self):
        i=0
        pesi=0
        for exam in self.lista_esami:
            i+=1
            peso=exam.calculate_exam_weight()
            pesi+=peso
        return pesi/i


    def calculate_average(self):
        i=0
        sum=0
        for exam in self.lista_esami:
            i+=1
            sum+=exam.voto
        return sum/i
