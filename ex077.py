palavras = ("carro", "casa","rua", "lua","planta","tinta","site",
            "onibus", "computador",)
for p in range (0, len(palavras)):
    print(f"Na palavra {palavras[p]} temos as vogais ")
    for letra in p:
        if letra in'aeiou':
            print(letra, end=' ')