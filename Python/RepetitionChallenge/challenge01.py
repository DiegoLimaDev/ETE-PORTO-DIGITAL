##This code asks for a number between 0 and 10 and checks if it's valid

i = int(input("Digite um número de zero a dez:\n"))
while(i <0 ) or (i > 10 ):
  i = int(input("Digite um número de zero a dez:\n"))
else:
  print("Você digitou: " + str(i))