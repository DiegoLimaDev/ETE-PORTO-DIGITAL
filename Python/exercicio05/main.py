nomes = []
print('Neste programa você digita o nome das pessoas que precisam ser cadastradas.')
adicionar = str(input('Digite o nome para o cadastro: '))
nomes.append(adicionar)
novo_nome = str(input('Deseja cadastrar outro nome? '))
while (novo_nome == 'sim'):
  adicionar = str(input('Digite o próximo nome: '))
  nomes.append(adicionar)
  novo_nome = str(input('Deseja cadastrar outro nome? '))
else:
  print(nomes)