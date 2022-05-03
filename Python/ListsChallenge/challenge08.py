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
