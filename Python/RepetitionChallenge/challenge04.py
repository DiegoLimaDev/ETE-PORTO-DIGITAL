##This code asks for the population for two cities and rate increase in the population

a = float(input("Digite a população da cidade A:\n"))
increaseA = float(input("Digite quantos '%' a população A cresce por ano:\n"))
while( increaseA <=0) or (increaseA > 100):
  increaseA = float(input("A resposta precisa ser entre 0 e 100. Digite novamente:\n"))
else:
  b = float(input("Digite a população da cidade B:\n"))
  increaseB = float(input("Digite quantos '%' a população B cresce por ano:\n"))
  while ( increaseB <=0) or (increaseB > 100):
      increaseA = float(input("A resposta precisa ser entre 0 e 100. Digite novamente:\n"))
  else:
    years = 0
    if(a < b):
      while(a < b):
        a = a + (a * (increaseA / 100))
        b = b + (b * (increaseB / 100))
        years += 1
      else:
        print("A população de A será maior que B em: " + str(years) + " anos.")
    else:
        while(b < a):
          a = a + (a * (increaseA / 100))
          b = b + (b * (increaseB / 100))
          years += 1
        else:
          print("A população de B será maior que A em: " + str(years) + " anos.")