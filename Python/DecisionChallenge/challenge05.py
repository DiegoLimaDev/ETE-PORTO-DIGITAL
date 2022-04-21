##This code asks for 3 numbers and prints the highest of them

x = float(input("Digite o primeiro número:\n"))
y = float(input("Digite o segundo número:\n"))
z = float(input("Digite o terceiro número:\n"))

if(x > z) and (x > y):
  print("O maior número é:" + str(x))
elif(z > x) and (z > y):
  print("O maior número é:" + str(z))
else:
  print("O maior número é:" + str(y))

