##Answer the questions with yes or no and see your possible participation in a crime

print("Utilize 'S' para sim ou 'N' para não nas perguntas a seguir:")
phoneCall = input("Você telefonou para a vítima?\n")
if(phoneCall != 'S') and (phoneCall != 'N'):
  print("Responda com 'S' ou 'N'.")
else:
  presence = input("Você esteve no local do crime?\n")
  if(presence != 'S') and (presence != 'N'):
    print("Responda com 'S' ou 'N'.")
  else:
    near = input("Você mora perto de vítima?\n")
    if(near != 'S') and (near != 'N'):
      print("Responda com 'S' ou 'N'.")
    else:
      owing = input("Você devia para a vítima?\n")
      if(owing != 'S') and (owing != 'N'):
        print("Responda com 'S' ou 'N'.")
      else:
        work = input("Já trabalhou com a vítima?\n")
        if(work != 'S') and (work != 'N'):
          print("Responda com 'S' ou 'N'.")
        else:

          answers = [phoneCall, presence, near, owing, work]
          counter = answers.count("S")
          if(counter == 2):
            print("Você é suspeito de cometer o crime.")
          elif(counter == 3) or (counter == 4):
            print("Você é considerado cúmplice no crime.")
          elif(counter == 5):
            print("Você é o culpado do crime.")
          else:
            print("Vocẽ é inocente.")