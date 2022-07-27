print('-'*30)
print("Sequencia de Fibonacci")
print('-'*30)
num = int(input("Quantos termos você quer mostrar? "))
print('~'*50)
cont = 3
x = 0
y = 1
print("0 -> {}".format(y), end=" -> ")
while cont <= num:
    r = x + y
    x = y
    y = r
    print("{}".format(r), end=" -> ")
    cont += 1
print("fim")
print("~"*50)

