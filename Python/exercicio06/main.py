names = []
ages = []

for i in range (0,5):
  add_name = str(input('Digite o nome da pessoa: '))
  names.append(add_name)
  print(names)

for i in range (0,5):
  add_age = int(input('Digite a idade da pessoa: '))
  ages.append(add_age)
  print(ages)
  print(sorted(ages, reverse = True))

