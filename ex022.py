#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maisculas é:{}".format(nome.upper()))
print("Seu nome em minusculas é {}".format(nome.lower()))
print("Seu nome ao todo tem {} letras".format(len(nome)- nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))