#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
opcão = " "
cont = ("zero","um", "dois","tres","quatro","cinco",
        "seis", "sete", "oito", "nove", "dez", "onze",
        "doze", "treze", "quatorze", "quinze", "deseseis",
        "deseste", "desoito", "desenove", "vinte")

while True:
    num =int(input("DIGITE UM NÚMERO entre 0 e 20."))
    if 0<= num <=20:
        break
    print("tente novamente.")
    while True:
        opcão = input("quer continuar s/n".upper())
        if opcão == "S":
            num = int(input("DIGITE UM NÚMERO entre 0 e 20."))
        elif opcão == "N":
            break
        else:
            print("opcação invalida tente novamente. Quer continuar [S/N]")

print(cont[num])
