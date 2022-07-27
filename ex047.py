#Exercício Python 47: Crie um programa que mostre na
# tela todos os números pares que estão no intervalo entre 1 e 50.

for count in range(2,51, 2):
    if (count % 2 == 0):
        print("{}".format(count))
print("acabou")