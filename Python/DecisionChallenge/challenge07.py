##This codes asks for three prices and prints the smallest of them

x = float(input("Digite o primeiro preço:\n"))
y = float(input("Digite o segundo preço:\n"))
z = float(input("Digite o terceiro preço:\n"))

if(x < y) and (x < z):
  print("O menor preço é: " + str(x))
elif(y < x) and (y < z):
  print("O menor preço é: " + str(y))
else:
  print("O menor preço é: " + str(z))