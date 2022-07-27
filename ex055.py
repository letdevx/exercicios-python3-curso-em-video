#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.


menor_peso = 500
maior_peso = 0

for cont in range (1,6):
    peso = int(input("Peso {} pessoa:".format(cont)))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print ("o maior peso é {} e o menor peso é {}".format(maior_peso,menor_peso))