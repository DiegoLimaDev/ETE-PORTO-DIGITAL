##This code asks for a year and checks if it is leap year

year = int(input("Digite o ano a ser verificado:\n"))
leap = year % 4
if(year > 0):
  if(leap == 0):
    print("O ano " + str(year) + " é bissexto.")
  else:
    print("O ano " + str(year) + " não é bissexto.")
else:
  print("Ano digitado inválido.")