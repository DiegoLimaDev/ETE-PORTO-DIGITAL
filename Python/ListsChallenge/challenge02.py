##This code asks for 10 real numbers, makes a list with them and print on the inverse order

numbers = []
for i in range (0, 10):
  addNumber = float(input("Digite o número a ser adicionado:\n"))
  numbers.append(addNumber)

numbers.reverse()
print(numbers)