termo_1 =int(input("digite o primeiro termo"))
razao = int(input("digite a razao"))
termo = termo_1
cont = 1
while cont <= 10:
    cont = cont + 1
    termo += razao
    print("{}".format(termo), end=" -> ")
print('Fim')