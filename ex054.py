#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for c in range(1,8):
    ano_nascimento = int(input("Em que ano a {} pessoa nasceu? ".format(c)))
    idade =  ano_atual - ano_nascimento
    if idade > 18 :
        maior_idade = maior_idade + 1
    elif idade < 18 :
        menor_idade = menor_idade + 1
print("Ao todo tivemos {} pessoas maiores de idade\nE tambem tivemos {} pessoas menores de idade".format(menor_idade, menor_idade))