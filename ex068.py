#Exercício Python 68: Faça um programa que jogue par ou ímpar
# com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

num = 0
opcao = "PpIi"
cont = 0
computador = random.Random
jogador = num
soma = 0
par = 0
impar = 0
opcao_usuario = ""
opcao_computador= ""
print("=-"*30)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*30)
while True:
    num = int(input("Diga um valor: "))
    opcao_usuario = input("Par ou Impar [P/I]")
    cont += 1
    computador = random.randint(0,10)
    soma = num + computador
    print('=' * 30)
    print(f"voce jogou {num} e o computador jogou {computador} total de {soma} deu", )
    print('=' * 30)

    if soma %2 == 0:
        par = soma
        print("par")
    else:
        impar = soma
        print("impar")

    if opcao_usuario == "P" or opcao_usuario == "p" and par == soma:
        print("voce venceu")
        print("Vamos jogar novamente...")
    elif opcao_usuario == "I" or opcao_usuario == "i" and impar == soma:
        print("voce venceu")
        print("Vamos jogar novamente...")

    else:
        break
print('='*15)
print(f"GAME OUVER! VOCE VENCEU {cont} VEZES")