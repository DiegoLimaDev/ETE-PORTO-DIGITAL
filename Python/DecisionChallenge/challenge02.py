##This code asks for a number and shows if it is positive, negative or neutral

x = float(input("Digite um número:\n"))

if(x > 0):
  print("O número " + str(x) + " é positivo.")
elif(x < 0):
  print("O número " + str(x) + " é negativo.")
else:
  print("O número " + str(x) + " é neutro.")

