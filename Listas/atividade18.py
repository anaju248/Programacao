hora_normal = 10
hora_extra = 15
hora_normal = int(input("Escreva as horas normais trabalhadas ")) 
hora_extra = int(input("Escreva as horas extras trabalhadas ")) 

salario_bruto = (hora_normal * 10) + hora_extra * 15
print(f"O salario bruto é: {salario_bruto} ")
sl = (hora_normal * 10) * 0.10
sl = (hora_normal * 10) - sl
sl = (hora_extra * 10) * 0.10


print(f"O salario liquido é: {sl}")