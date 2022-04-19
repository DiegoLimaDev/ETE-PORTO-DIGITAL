##This code asks how much a person receives per hour of work and how many hours have been
##this month to calculates the total amount of money

moneyPerHour = float(input("Quanto você ganha por hora trabalhada?\n"))
hours = int(input("Quantas horas você trabalhou neste mês?\n"))
total = moneyPerHour * hours
print("Seu salário esse mês é: " + str(total))