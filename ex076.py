produtos = ("lapis",1.75,
            "borracha", 2.00,
            "caderno", 15.90,)
cont = 0
print("-"*40)
print(f'{"listagem de preços":^}')
print("-"*40)
for cont in range (0, len(produtos)):
    if cont %2== 0:
        print(f"{produtos[cont]:.<30}", end='')
    else:
        print(f'R${produtos[cont]:>7.2f}')
print("-"*40)
