#altura e sexo dessa pessoa(M ou F) M peso ideal é 72,7   F peso ideal  
h = float(input("insira a altura  em centimetros"))
sexo = float(input("insira o seu sexo (sexo(m ou f))"))
if sexo == "m":
    peso_ideal = (72,7*h) - 58
    print("para homens o pesoideal é:", peso_ideal)
elif sexo == "F":
    peso_ideal = (62,1*h) - 44,7
    print("para mulheres o pesoideal é:", peso_ideal)
else
    print("sexo invalidopor favor insira M")

