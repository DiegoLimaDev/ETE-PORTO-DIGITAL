##This code asks for 4 numbers and shows the media

numbers = []
for i in range(0, 4):
  addNumber = float(input("Digite o número a ser utilizado no cálculo de média:\n"))
  numbers.append(addNumber)

print(numbers)
print('A sua média é: ' + str(sum(numbers) / 4))