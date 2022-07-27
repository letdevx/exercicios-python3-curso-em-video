
termo_1 =int(input("digite o primeiro termo"))
razao = int(input("digite a razao"))
decimo = termo_1 +(10-1) * razao
for c in range(termo_1, decimo, razao):
    print("{}".format(c), end= " -> ")