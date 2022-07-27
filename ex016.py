#Exercício Python 16: Crie um programa que leia um número
# Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math #importação completa da biblioteca
num = float(input("Digite um número com virgula: "))
parte = math.trunc(num)
print ("A parte inteira de {} é igual a:{}".format(num, parte))

from math import trunc #importação somente da função trunc
num = float(input("Digite um número com virgula: "))
parte = trunc(num)
print ("O número digitado foi {} e sua pate inteira é: {}".format(num,parte))