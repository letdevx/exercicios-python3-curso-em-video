soma = 0
produto_mais_caro = 0
produto_mais_barato = 500000000000000000000000000000000000000000
nome_produto_mais_barato = ''
print("-"*50)
print("loja super baratão")
print('-'*50)
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço:R$ "))
    soma += preco
    if preco > 1000:
        produto_mais_caro += 1
    if preco < produto_mais_barato:
        produto_mais_barato = preco
        nome_produto_mais_barato = produto
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar [S/N]?")).strip().upper()[0]
    if opcao == 'N':
        break
print("------------FIM DO PROGRAMA----------------")
print(f"O totatal da compra foi {soma}")
print(f"Temos {produto_mais_caro} produtos custando mais de 1000")
print(f"O produto mais barato foi {nome_produto_mais_barato} que custa {produto_mais_barato}")