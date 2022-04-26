##This code asks how much a collector spent in his collection and calculates the media and the price per item

amount = int(input("Quantos CDs tem sua coleção?\n"))
cds = []


for i in range(0, amount):
  cdPrices = int(input("Digite o preço de cada CD que você comprou:\n"))
  cds.append(cdPrices)

print("O valor total gasto na sua coleção é: " + str(sum(cds)))
print("A média gasta por CD é: " + str(sum(cds)/amount))