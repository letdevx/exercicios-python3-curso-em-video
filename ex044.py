#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
print("+="*30, "lojas Guanabara","+="*30)
preco_compras = float(input("Valor da compra: "))
print('''Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista cartão 
[3] 2x no cartão
[4] 3x ou mais  no cartão''')
opcao = int(input("Digite a sua opção"))
if opcao == 1 == 2 == 3:
    opcao = int(input("Digite a sua opção"))
else:
    opcao = int(input("Digite a sua opção"))
    numero_parcelas = int(input("Quantas parcelas?"))

if opcao == 1:
  desconto_avista =  preco_compras -(preco_compras*10/100)
  print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco_compras, desconto_avista))
elif opcao == 2:
    desconto_cartão = preco_compras-(preco_compras*5/10)
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco_compras, desconto_cartão))
elif opcao == 3:
    print("Sua compra de vai custar {:.2f}".format(preco_compras))
elif opcao == 4:
    adicao_cartao = preco_compras + (preco_compras*20/100)
    valor_parcela = adicao_cartao / numero_parcelas
    print('''Sua compra sera parcelada {}x de  R${} com jurus 
sua compra vai custar {:.2f} no final '''.format(numero_parcelas, valor_parcela,adicao_cartao))
else:
    print("Opcão invalida tente novamente")