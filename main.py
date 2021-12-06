#Izveidot funkciju, kas pārbauda, vai skaitlis atroda lietotāja noteiktā diapazonā vai nē.
def noteiktDiapazonu(d1,d2,sk):                             
  rezultats = "Skaitlis nav diapazonā!"
  if d2>=sk<=d2:
    rezultats = "Skaitlis ir diapazonā!"
  return rezultats

d1 = int(input("Ievadi diapazona sākumu:"))
d2 = int(input("Ievada diapazona beigas: "))
sk = int(input("Ievadi skaitli: "))
rez = noteiktDiapazonu(d1,d2,sk) 
print(rez)