##This code reads three numbers and prints them descending

numbers = []

for i in range(0 , 3):
  addNumber = float(input("Digite um número:\n"))
  numbers.append(addNumber)

print("A ordem descrente é: " + str((sorted(numbers, reverse = True))))