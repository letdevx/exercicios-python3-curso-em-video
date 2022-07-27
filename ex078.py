valores = list()
for cont in range (0, 5):
    valores.append(int(input(f"digite um número na posição {cont} : ")))
print("=*"* 30)
print(f"voce digitou os valores {valores }")
print(f"o maior valor digitado foi: {max(valores)} nas posicoes ", end= '')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f"{i}...", end=' ')
print(f"O menor valor digitado foi: {min(valores)} nas posiçoes ", end=' ')
for i, v in enumerate(valores):
   if v == min(valores):
    print(f"{i}...", end=' ')

