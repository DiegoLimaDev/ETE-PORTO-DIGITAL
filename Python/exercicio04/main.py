pousado = input('O avião está pousado? Responda com sim ou nao, por favor.\n')
if pousado == 'nao':
  speed = int(input('Qual sua velocidade atual do avião?\n'))
  if speed < 500:
    print('Você precisa acelerar.')
  elif speed == 500:
    print('Mantenha sua velocidade.')
  else:
    print('Você precisa desacelerar.')
  
  height = int(input('Qual a altura atual do avião?\n'))
  if height < 1000:
    print('O avião precisa estar em maior altitude.')
  elif height == 1000:
    print('Mantenha a sua altitude.')
  else:
    print('O avião precisa estar em menor altitude.')

  if (speed == 500) and (height == 1000):
    print('Você está em condições ideais. Ative o piloto automatico.')
  else:
    print('Ajuste suas condições antes de ativar o piloto automatico.')
    
elif pousado == 'sim':
  print('Você precisa decolar.')

else:
  print('Sua resposta não satisfaz o programa.')
