peso_queijo = 50
peso_presunto = 50
peso_burguer = 100

quantidade_sanduiche =int(input("Digite a quantidade de sanduiches: "))

peso_queijo_total = quantidade_sanduiche * (peso_queijo * 2)
peso_presunto_total = quantidade_sanduiche * peso_presunto
peso_burguer_total = quantidade_sanduiche * peso_burguer

peso_queijo_totalKg = peso_queijo_total / 1000
peso_presunto_totalKg = peso_presunto_total / 1000
peso_burguer_totalKg = peso_burguer_total / 1000

print(f"peso total queijo{peso_queijo_totalKg}")
print(f"peso total presunto{peso_presunto_totalKg}")
print(f"peso total burguer{peso_burguer_totalKg}")
