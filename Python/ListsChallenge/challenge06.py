##This code makes a list with students grades medias and checks how many students are above media 7

medias = []
for i in range(0, 2):
  n1 = float(input("Digite a primeira nota do aluno:\n"))
  n2 = float(input("Digite a segunda nota do aluno:\n")) 
  n3 = float(input("Digite a terceira nota do aluno:\n"))
  n4 = float(input("Digite a quarta nota do aluno:\n"))
  print('Agora o sistema necessita das notas do aluno seguinte.\n')
  media = (n1 + n2 + n3 + n4) / 4
  medias.append(media)

mediasAboveSeven = []
for i in range(0, len(medias)):
  if(medias[i] >= 7):
    mediasAboveSeven.append(medias[i])

if(len(mediasAboveSeven) == 1):
  print(str(len(mediasAboveSeven)) + ' aluno ficou com média maior ou igual a 7.')
else:
    print(str(len(mediasAboveSeven)) + ' alunos ficaram com média maior ou igual a 7.')