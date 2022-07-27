#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
a = int(input("um numero inteiro"))
b = int(input("digite outro numero inteiro"))

if a > b:
    print("O maior numero é {}".format(a))
elif a < b:
    print("O maior numero é {}".format(b))
elif a == b:
    print("Os numeros são iguais")