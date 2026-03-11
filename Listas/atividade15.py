total= float(input("Total a pagar: "))

valor_por_pessoa = total / 3

carlos =int(valor_por_pessoa)
andre = int(valor_por_pessoa)

felipe = total - (carlos + andre)

print("Carlos deve pagar R${:.2f}". format( carlos))
print("André deve pagar R${:.2f}". format(andre))
print("Felipe deve pagar R${:.2f}". format(felipe))