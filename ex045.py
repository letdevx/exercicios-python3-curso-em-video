#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pedra = 0
papel = 1
tesoura = 2
print('''Suas opçoes
[1]pedra
[2]Papel
[3] Tesoura''')
comp = random.randint(0, 2)
jogador = int(input("Qual é a sua jogada? "))
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1 )
print("Po!!!")
print("-=" * 30)
print("computador jogou {}".format(itens[comp]))
print("jogador jogou {}".format(itens[jogador]))
print("-=" * 30)
if jogador == pedra and comp == papel:
    print("Computador ganha")
elif jogador == pedra and comp == pedra:
    print("empate")
elif jogador == pedra and comp == tesoura:
    print("jogador ganha")
elif jogador == papel and comp == pedra:
    print("jogador ganha")
elif jogador == papel and comp == papel:
    print("empate")
elif jogador == papel and comp == tesoura:
    print("computador ganha")
elif jogador == tesoura and comp == papel:
    print("jogador ganha")
elif jogador == tesoura and comp == tesoura:
    print("empate")
elif jogador == tesoura and comp == pedra:
    print("computador ganha")
else:
    print("opção invalida")


