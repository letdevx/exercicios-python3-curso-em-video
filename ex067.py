#Exercício Python 067: Faça um programa que mostre a
# tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
num = int(input("digite um número"))
tab = 0

while True:
    print('='*30)
    for c in range (1,11):
        tab = c * num
        print(f"{c} * {num} = {tab} ")
    num = int(input("Quer ver a tabuada de qual número?"))
    if num < 0:
        break
    print('=' * 30)
print("")