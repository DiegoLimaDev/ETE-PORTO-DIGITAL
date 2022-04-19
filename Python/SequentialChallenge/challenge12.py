##This code uses a height of a person to calculates the ideal weight

height = float(input("Qual a altura para o cálculo do imc?\n"))
idealWeight = (72.7 * height) - 58
print("O peso ideal para a altura " + str(height) + " é: " + str(idealWeight) + "kgs")