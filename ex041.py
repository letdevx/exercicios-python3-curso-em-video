#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Qual seu ano de nascimento?"))
idade = ano_atual - ano_nascimento
print("O atleta tem {} anos".format(idade))
if idade <= 0 and idade <= 9:
    print("MIRIM")
elif idade >= 10 and idade <= 14:
    print("IFANTIL")
elif idade >= 15 and idade <= 19:
    print("JÚNIOR")
elif idade >= 20 and idade <= 25:
    print("SENIOR")
else:
    print("MASTER")