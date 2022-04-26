##This code asks for five numbers and print the sum and the media of them

numbers = []
for i in range(0, 5):  
  number = float(input("Digite um número:\n"))
  numbers.append(number)  

print("A soma dos números é: " + str(sum(numbers)))
print("A média dos números é: " + str(sum(numbers)/len(numbers)))