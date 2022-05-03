##This code asks for five numbers and shows the sum and the multiplication between them

numbers = []
for i in range(0, 5):
  addNumber = int(input('Digite o número a ser adicionado:\n'))
  numbers.append(addNumber)

print(numbers)
print('A somo de todos os números é : ' + str(sum(numbers)))

product = 1
for i in range(0, len(numbers)):
  product *= numbers[i]

print('A multiplicação de todos os números é: ' + str(product))