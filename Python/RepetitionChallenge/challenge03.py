##This code makes a calcule of two populations and how many years will take to A be higher than B

a = 80000
b = 200000
years = 0
while(a < b):
  a = a + (a * 0.03)
  b = b + (b * 0.015)
  years += 1
else:
  print("A população de A será maior que B em: " + str(years) + " anos.")