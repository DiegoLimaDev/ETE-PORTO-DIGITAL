##This code prints de odd numbers between 0 and 50

x = 1
numbers = []
for i in range (0 , 50):
  if(x % 2 != 0):
    numbers.append(x)

  x += 1

print(numbers)