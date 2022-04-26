##This code deals with two lists

students = []
heights = []
for i in range (0, 10):
  addStudents = str(input("Adicione o número estudante:\n"))
  students.append(addStudents)
  addHeights = float(input("Agora sua respectiva altura:\n"))
  heights.append(addHeights)

x = heights.index(max(heights))
y = students[x]
print("O maior aluno foi cadastrado com o número: " + str(y) + ". Medindo respectivamente: " + str(max(heights)))
