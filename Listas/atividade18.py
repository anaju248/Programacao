hora_normal = 10
hora_extra = 15
hora_normal = int(input("Escreva as horas normais trabalhadas ")) 
hora_extra = int(input("Escreva as horas extras trabalhadas ")) 

salario_bruto = (hora_normal * 10) + (hora_extra * 15)
print(f"O salario bruto é: {salario_bruto} ")
sb = (hora_normal * 10) * 0.10
sb = (hora_normal * 10) - sb

print(f"O salario liquido é: {sb}")