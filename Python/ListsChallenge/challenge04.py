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