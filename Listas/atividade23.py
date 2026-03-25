altura_pessoa = float(input("Digite sua altura "))
sombra_pessoa = float(input("Digite o comprimento da sua sombra"))
sombra_predio = float(input("Digite a sombra do predio"))
altura_predio = (altura_pessoa / sombra_pessoa) * sombra_predio
print ("A aultura do predio é", altura_predio)