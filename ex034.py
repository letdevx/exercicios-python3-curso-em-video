#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o valor do salario atual R$ "))

if salario <= 1250:
   novo = salario + (salario * 10/100)
else:
  novo = salario + (salario * 15/100)

print("Quem ganhava R${} passa a ganhar R${}".format(salario, novo))