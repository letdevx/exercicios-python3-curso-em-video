#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
print('--=' * 50)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('--=' * 50)
sorteio = random.randint(0, 5)
num = int(input("Em que número eu pensei ? ") )
print("PROCESSANDO...")
sleep(3)
if num == sorteio:
     print("PARABÉNS VOCÊ CONSEGUIU ME VENCER! ")
else:
    print("Ganhei! Eu pensei no número {}".format(sorteio))