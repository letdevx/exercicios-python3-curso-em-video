#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# ]No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
opcao ="sSnN"
while True:
    valor = input("Digite um valor: ")
    if valor not in valores:
        valores.append(valor)
    else:
        print("Valor duplicado! não vou adicionar...")

    opcao = input("Quer continuar?[s/n]").upper()
    if opcao == "N":
        break

print("*"*30)
valores.sort()
print(f"valores {valores}")