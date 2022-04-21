##This code asks for a date and checks if it is valid

print("Digite um data a partir do primeiro com 4 dígitos, ou seja, a partir do primeiro milênio.")
day = int(input("Qual o dia?\n"))
if(day < 1 ) or (day > 31):
  print("Dia digitado inválido.")
else:
  month = int(input("Qual o mês?\n"))

  if(month < 1) or (month > 12):
    print("Mês digitado inválido.")
  else:
    year = int(input("Qual o ano?\n"))
    
    if(year < 1000):
      print("Ano digitado inválido.")
    else:
      if(month == 2) and (year % 4 != 0) and (day > 28):
        print("O mês de fevereiro tem apenas 28 dias em anos não bissextos.")
      elif(month == 2) and (year % 4 == 0) and (day > 29):
        print("O mês de fevereiro não tem mais que 29 dias.")
      elif(month == 4, 6, 9, 11) and (day > 30):
        print("O mês digitado possui apenas 30 dias.")
      else:
        print("A data digitada foi: " + str(day) + "/" + str(month) + "/" + str(year))