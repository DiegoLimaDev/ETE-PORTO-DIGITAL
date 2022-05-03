##This code asks for 20 integer numbers and checks if they are pair or odd

numbers = []
oddNumbers = []
pairNumbers = []

for i in range(0, 20):
  addNumber = int(input('Digite um número a ser adicionado:\n'))
  numbers.append(addNumber)

print(numbers)

for i in range(0, len(numbers)):
  if(numbers[i] % 2 == 0):
    pairNumbers.append(numbers[i])
  else:
    oddNumbers.append(numbers[i])

print("Os números pares são: " + str(pairNumbers))
print("Os números ímpares são: " + str(oddNumbers))