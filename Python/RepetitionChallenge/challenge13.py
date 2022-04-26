##This code makes a list and checks numbers in certain range

numbers = []
addNumber = 0
while(addNumber >= 0):
  addNumber = float(input("Digite um número:\n"))
  numbers.append(addNumber)

filter0_25 = []
for i in numbers:
  if(0 <= i <= 25):
    filter0_25.append(i)
print("A quantidade de números entre 0 e 25 é: " + str(len(filter0_25)))

filter26_50 = []
for i in numbers:
  if(26 <= i <= 50):
    filter26_50.append(i)
print("A quantidade de números entre 0 e 25 é: " + str(len(filter26_50)))

filter51_75 = []
for i in numbers:
  if(51 <= i <= 75):
    filter51_75.append(i)
print("A quantidade de números entre 0 e 25 é: " + str(len(filter51_75)))

filter76_100 = []
for i in numbers:
  if(76 <= i <= 100):
    filter76_100.append(i)
print("A quantidade de números entre 0 e 25 é: " + str(len(filter76_100)))