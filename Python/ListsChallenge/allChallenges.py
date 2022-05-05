##Challenge01
##This code asks for 5 numbers and makes a list with them

numbers = []
for i in range(0, 5):
  addNumber = int(input("Digite um número para ser adicionado:\n"))
  numbers.append(addNumber)

print(numbers)

##Challenge02
# ##This code asks for 10 real numbers, makes a list with them and print on the reverse order

numbers = []
for i in range (0, 10):
  addNumber = float(input("Digite o número a ser adicionado:\n"))
  numbers.append(addNumber)

numbers.reverse()
print(numbers)

##Challenge03
##This code asks for 4 numbers and shows the media

numbers = []
for i in range(0, 4):
  addNumber = float(input("Digite o número a ser utilizado no cálculo de média:\n"))
  numbers.append(addNumber)

print(numbers)
print('A sua média é: ' + str(sum(numbers) / 4))

##Challenge04
##This codes asks for 10 characters and checks if they are consonants

characters = []
consonants = []
for i in range (0, 10):
  addCharacter = str(input("Digite um caractere alfabético para ser adicionado à lista:\n"))
  while(len(addCharacter) != 1):
    addCharacter = str(input("Por favor, digite apenas um caractere alfabético:\n"))
  else:
    characters.append(addCharacter)

for i in range (0, len(characters)):
  if(characters[i] != 'a') and (characters[i] != 'e') and (characters[i] != 'i') and (characters[i] != 'o') and (characters[i] != 'u'):
    consonants.append(characters[i])

print('Você digitou ' + str(len(consonants)) + ' consoantes.')
print(consonants)

##Challenge05
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

##Challenge06
##This code makes a list with students grades medias and checks how many students are above media 7

medias = []
for i in range(0, 2):
  n1 = float(input("Digite a primeira nota do aluno:\n"))
  n2 = float(input("Digite a segunda nota do aluno:\n")) 
  n3 = float(input("Digite a terceira nota do aluno:\n"))
  n4 = float(input("Digite a quarta nota do aluno:\n"))
  print('Agora o sistema necessita das notas do aluno seguinte.\n')
  media = (n1 + n2 + n3 + n4) / 4
  medias.append(media)

mediasAboveSeven = []
for i in range(0, len(medias)):
  if(medias[i] >= 7):
    mediasAboveSeven.append(medias[i])

if(len(mediasAboveSeven) == 1):
  print(str(len(mediasAboveSeven)) + ' aluno ficou com média maior ou igual a 7.')
else:
    print(str(len(mediasAboveSeven)) + ' alunos ficaram com média maior ou igual a 7.')

##Challenge07
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

##Challenge08
##This code asks for 5 names and 5 heights and prints the reverse order inputed

names = []
heights = []

for i in range(0, 5):
  name = str(input('Digite o nome da pessoa:\n'))
  names.append(name)
  height = float(input('Digite a altura da respectiva pessoa:\n'))
  heights.append(height)

names.reverse()
heights.reverse()
print('A ordem inversa dos nomes é: ' + str(names))
print('A ordem inversa das alturas é: ' + str(heights))

##Challenge09
##This code asks for 10 numbers and calculates the sum of them squared

numbers = []
for i in range(0, 10):
  addNumber = int(input('Digite o número a ser adicionado:\n'))
  numbers.append(addNumber)

product = 0
for i in range(0, len(numbers)):
  product += (numbers[i] ** 2)

print('A soma dos quadrados dos elementos é: ' + str(product))

##Challenge10
##This codes makes two lists and prints a third list with the elements interleaved

numbers = []
characters = []

for i in range(0, 10):
  addNumber = int(input('Digite um valor inteiro para ser adicionado:\n')) 
  numbers.append(addNumber)

for i in range(0, 10):
  character = str(input('Digite um caracter para ser adicionado:\n'))
  while(len(character) != 1):
    character = str(input('Por favor, digite apenas um caracter:\n'))
  else:
    characters.append(character)

group = []
for i in range(0, len(numbers)):
  group.insert(len(group), numbers[i])
  group.insert(len(group), characters[i])

print(group)