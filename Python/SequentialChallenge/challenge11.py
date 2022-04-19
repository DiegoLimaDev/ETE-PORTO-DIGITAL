##This code asks for 2 int numbers and 1 real number and calculates multiples operations
##between them

n1 = int(input("Digite o primeiro número inteiro:\n"))
n2 = int(input("Digite o segundo número inteiro:\n"))
n3 = float(input("Digite o número real:\n"))
operation1 = (n1 * 2) * (n2 / 2)
print("O valor do produto do dobro do primeiro com a metade do segundo é: " + str(operation1))
operation2 = (n1 * 3) + (n3)
print("O valor da soma do triplo do primeiro com o terceiro é: " + str(operation2))
operation3 = n3 ** 3
print("O valor do terceiro elevado ao cubo é : " + str(operation3))


