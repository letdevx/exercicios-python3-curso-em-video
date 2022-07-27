#Exercício Python 18: Faça um programa que leia um ângulo
# qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

import math
angulo = float(input("Didite o valor do agulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("Para o angulo digitado de {}".format(angulo))
print('='* 30)
print("o seno é {:.2f}".format(seno))
print ("o cosseno é {:.2f}".format(cosseno))
print("a tangente é {:.2f}".format(tangente))
print('='*30)