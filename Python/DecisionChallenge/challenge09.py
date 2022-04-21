##This code asks the time of your class

shift = str(input("Qual horário da sua aula? Digite uma das respostas válidas.\nM - Matutino\nV - Vespertino\nN - Noturno\n"))
if(shift == 'M') or (shift == 'm'):
  print("Bom dia!")
elif(shift == 'V') or (shift == 'v'):
  print("Boa tarde!")
elif(shift == 'N') or (shift == 'n'):
  print("Boa noite!")
else:
  print("Turno inválido.")