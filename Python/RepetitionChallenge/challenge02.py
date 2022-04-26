##This code asks for a name and a password and checks if they are the same

name = str(input("Digite seu nome:\n"))
password = str(input("Digite sua senha:\n"))
while(name == password):
  password = str(input("Sua senha não pode ser igual ao seu nome. Digite uma senha nova:\n"))
else:
  print("Cadastro feito com sucesso.")