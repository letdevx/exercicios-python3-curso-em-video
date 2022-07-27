termo_1 =int(input("digite o primeiro termo"))
razao = int(input("digite a razao"))
termo = termo_1
cont = 0
while cont <= 10:
    cont = cont + 1
    termo += razao
    print("{}".format(termo), end=" -> ")
    novos_termos = int(input("\nquantos termos você quer mostrar a mais ?"))
     for c in range (0,novos_termos):


print('Fim')

