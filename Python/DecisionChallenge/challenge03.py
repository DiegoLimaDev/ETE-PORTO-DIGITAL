##This code checks if the character inputed is F or M

x = str(input("Qual seu gênero? Considere 'F' ou 'M' como resposta.\n"))
if(x == 'F'):
  print("O gênero é feminino.")
elif(x == 'M'):
  print("O gênero é masculino.")
else:
  print("Gênero invalido.")