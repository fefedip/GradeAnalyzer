class Esame:
     def __init__ (self, nome, cfu, voto):
          self.nome=nome
          self.cfu=cfu
          self.voto=voto

     def calculate_exam_weight(self):
          return self.voto * self.cfu
     