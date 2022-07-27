#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input("digite um numero"))
resultado = num
print('calculando {}! ='.format(resultado), end='')
while (num > 1):
    num = num -1
    resultado = resultado * num
    print("{}".format(num,), end='')
    print(' x ' if num > 1 else ' = ', end='')
print("{}".format(resultado))