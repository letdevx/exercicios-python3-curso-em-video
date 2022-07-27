# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Digite um numero inteiro:"))
print('''Escolha uma das bases pra conversão:
[1]binario
[2]octal
[3]hexadecimal''')
opção = int(input("sua opção: "))

if opção == 1:
    binario = bin(num)
    print("O numero {} convertido para binário {} é".format(num, binario [2:]))
elif opção == 2:
    octal = oct(num)
    print("O numero {} convertido para octal é {}".format(num, octal [2:]))
elif opção == 3:
    hexadecimal = hex(num)
    print("O numero {} convertido para hexadecimal é {}".format(num, hexadecimal [2:]))
else:
    print("opção invalida tente novamente")
