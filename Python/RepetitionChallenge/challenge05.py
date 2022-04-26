##This code use a counter to print from 1 to 20

counter = 1
numbers = []
for i in range(0,20):
  print(counter)
  numbers.append(counter)
  counter += 1

print(numbers)