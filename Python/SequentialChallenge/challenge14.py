##This code use a rule that if a fisher catches more than 50kg in a run he has to pay a surplus price
##using this rule the code print the excesse amount and the price to be paid

fishingAmount = float(input("Quantos quilos de peixe foram pescados?\n"))
if(fishingAmount < 50):
  print("Não há multa para quantias menores que 50kgs")

else:
  overrun = fishingAmount - 50
  print("O valor em quilos excedente do permitido é: " + str(overrun))
  priceOverrun = overrun * 4
  print("O valor a ser pago devido a pesca excedente é: " + str(priceOverrun))
