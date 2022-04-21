##This code asks for two numbers and prints the highest of them

x = float(input("Digite o primeiro número:\n"))
y = float(input("Digite o segundo número:\n"))

if(x > y):
  print("O maior número é: " + str(x))
elif(y > x):
  print("O maior número é: " + str(y))
else:
  print("Os números são iguais.")
