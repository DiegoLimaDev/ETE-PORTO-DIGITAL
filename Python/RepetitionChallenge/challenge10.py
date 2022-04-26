##This code asks for two numbers and print the sum of the numbers between them

x = int(input("Digite um número inteiro:\n"))
y = int(input("Digite outro número inteiro:\n"))
while( x == y):
  y = int(input("Os números precisam ser diferentes. Digite outro número inteiro:\n"))
else:
  numbers = []
  if (x < y):
    while(x < y):
      x += 1
      if(x < y):
        numbers.append(x)

    print("A soma dos números é: " + str(sum(numbers)))

  else:
    while(y < x):
      y += 1
      if(y < x):
        numbers.append(y)

    print("A soma dos números é: " + str(sum(numbers)))
