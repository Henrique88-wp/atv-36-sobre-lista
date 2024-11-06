#Ler uma lista com 4 notas, em seguida 
#o programa deve exibir as notas e a 
#média

nota = []
med= [] 

for i in range(4):
    a = float(input(f"Coloque a nota {i+1}:"))
    nota.append(a)

b = (sum(nota) / len(nota))
med.append(b)

print(f" A suas notas são: {nota}")
print(f"a sua média é: {med}")