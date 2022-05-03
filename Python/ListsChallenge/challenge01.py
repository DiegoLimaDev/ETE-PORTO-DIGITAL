##This code asks for 5 numbers and makes a list with them

numbers = []
for i in range(0, 5):
  addNumber = int(input("Digite um número para ser adicionado:\n"))
  numbers.append(addNumber)

print(numbers)