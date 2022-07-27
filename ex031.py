#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Digite a distancia da viagem em km: "))
viagem_200km = distancia * 0.50
viagem_201km = distancia * 0.45
if distancia <= 200:
    print("O valor da passagem é R${:.2f}".format(viagem_200km))
else:
    print("O valor da passagem é R${:.2F}".format(viagem_201km))