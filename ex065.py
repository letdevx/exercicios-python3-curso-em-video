#Exercício Python 65: Crie um programa que leia vários números
# inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

opcao = "s" .upper()
soma = 0
maior = 0
menor = 0
cont = 0
while opcao in "Ss".upper():
    num = int(input("Digite um número: "))
    opcao = input("Quer continuar? [S/N]".upper())
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print("Você digitou {} números e a media foi {} O maior número digitado foi {} o menor número foi {}".format(cont, media, maior, menor))
