#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idade_max = 0
nome_idade_max = ""
feminino_menor = 0
media = 0
for cont in range(1, 5):
    print('=' * 5, "{} pessoa ======".format(cont))
    nome = input("Nome: ")
    idade = int(input("Idade:"))
    sexo = input("[F/M]")
    media = media + idade
    if idade < 20 and sexo == "F":
        feminino_menor = feminino_menor + 1
    if idade > idade_max and sexo == "M":
        idade_max = idade
        nome_idade_max = nome
media = media / 4
print("A media de idade do grupo é {} anos".format(media))
print("O homem mais velho tem {} e se chama {}".format(idade_max, nome_idade_max))
print("Ao todo são {} molheres com menos de 20 anos".format(feminino_menor))
