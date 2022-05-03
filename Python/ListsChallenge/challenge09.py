##This code asks for 10 numbers and calculates the sum of them squared

numbers = []
for i in range(0, 10):
  addNumber = int(input('Digite o número a ser adicionado:\n'))
  numbers.append(addNumber)

product = 0
for i in range(0, len(numbers)):
  product += (numbers[i] ** 2)

print('A soma dos quadrados dos elementos é: ' + str(product))