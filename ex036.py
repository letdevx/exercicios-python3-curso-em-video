#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o valor do seu salario: R$"))
num_parcela = int(input("Em quantas vezes voce deseja pagar?"))
prestacao_mensal = valor_casa/num_parcela
print("para paga uma cada de {} em {} parcelas a prestação sera de {:.2f}". format(valor_casa,num_parcela,prestacao_mensal))
if prestacao_mensal >= salario * 30 / 100:
    print("emprestimo negado")
else:
    print("emprestimo aprovado")


