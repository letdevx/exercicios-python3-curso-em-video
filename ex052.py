#Exercício Python 52: Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.

# maior que 1;
# somente divisivel por 1 ou por ele mesmo; 
num = int(input("Digite um número inteiro"))
for c in range(1,num +1):
    if num > 1 and num % c == 0 and num % num == 0:
        print(c)