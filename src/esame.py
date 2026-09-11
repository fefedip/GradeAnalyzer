class Esame:
     def __init__ (self, esame, cfu, voto):
          self.esame=esame
          self.cfu=cfu
          self.voto=voto

     def __str__(self):
          return f"Esame: {self.esame} - CFU: {self.cfu} - Voto:{self.voto}"

     def calculate_exam_weight(self):
          return self.voto * self.cfu
     