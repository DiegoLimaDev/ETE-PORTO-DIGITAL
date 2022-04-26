##This code deals with a list of arithmetic progression 

numerator = 1
divider = 1
terms = int(input("Quantos termos você deseja nessa progressão?\n"))
operation = []

while(numerator <= terms):
  x = numerator / divider
  operation.append(x)
  numerator += 1
  divider += 2

print(operation)
print("\nA soma de todos os números da lista é: " + str(sum(operation)))