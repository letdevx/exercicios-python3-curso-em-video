#Exercício Python 29: Escreva um programa que leia a velocidade
# de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade atual do carro? "))
limite = 80
multa = (velocidade - limite) * 7.00
if velocidade <= limite:
    print("Tenha um bom dia dirija com segurança!")
else:
    print("Multado! Você excedeu o limite permitiso que é {}km/h. \nVoce deve pagar uma multa no valor de R${}".format(limite, multa))