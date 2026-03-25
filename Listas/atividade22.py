moedas_1_centavo = int(input("Digite a quantidade de moedas de 1 centavo"))
moedas_5_centavo = int(input("Digite a quantidade de moedas de 5 centavos"))
moedas_10_centavo = int(input("Digite a quantidade de moedas de 10 centavos"))
moedas_25_centavo = int(input("Digite a quantidade de moedas de 25 centavos"))
moedas_50_centavo = int(input("Digite a quantidade de moedas de 50 centavos"))
moedas_1_real = int(input("Digite a quantidade de moedas de 1 real"))
totais_reais = (moedas_1_centavo * 0.01) + \
    (moedas_5_centavo * 0.05) + \
     (moedas_10_centavo * 0.10) + \
        (moedas_25_centavo * 0.25) + \
              (moedas_50_centavo * 0.50) + moedas_1_real
print("O valor tota em reais", totais_reais)