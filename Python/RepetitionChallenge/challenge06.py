##This code asks for five numbers and prints the higher of them

numbers = []
for i in range(0, 5):  
  number = float(input("Digite um número:\n"))
  numbers.append(number)  

print("O maior número digitado foi: " + str(max(numbers)))