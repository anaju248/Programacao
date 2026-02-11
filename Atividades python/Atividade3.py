contador = 1
soma_notas = 0
while contador <= 4:
    nota = float(input(f"insira a nota do {contador} aluno"))
    soma_notas += nota
    contador +=1
media = soma_notas/4
print("A media das 4 notas é: ",media)