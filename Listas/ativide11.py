dias_trabalhados = int(input("dgite o númerode dias trabalhados sem acidentes"))
                
anos = dias_trabalhados // 365
meses = (dias_trabalhados % 365) //  30 
dias = (dias_trabalhados % 365) % 30

print(f"{dias_trabalhados}dias equivalem a {anos} anos, {meses} meses, e {dias} dias")