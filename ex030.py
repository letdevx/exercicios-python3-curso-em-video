#Exercício Python 30: Crie um programa que leia um número inteiro
# e mostre na
#tela se ele é PAR ou ÍMPAR.

num = int(input("Me diga um Número qualquer:"))
par = num % 2 == 0
impar = num % 3 <=1

if num % 2 == 0:
    print("O Número digitado é par!")
else:
    print("Número ímpar")