##This code calculates the ideal weight using the correct formula to men and women

gender = int(input("Qual seu gênero?\n1 - Feminino\n2 - Masculino\n"))
if(gender == 1):
  height = float(input("Qual sua altura?\n"))
  idealWeight = (62.1 * height) - 44.7
  print("O peso ideal para a altura " + str(height) + " é: " + str(idealWeight) + "kgs")

elif(gender == 2):
  height = float(input("Qual sua altura?\n"))
  idealWeight = (72.7 * height) - 58
  print("O peso ideal para a altura " + str(height) + " é: " + str(idealWeight) + "kgs")

else:
  print("Digite um código válido.")
