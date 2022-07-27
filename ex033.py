#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int (input("primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))
# verificando quem é menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor numero é: {} ".format(menor))
print("o mair numero é:{}".format(maior))