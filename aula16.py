lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
print(lanche[1]) #mostra o que está guardado na primeira posição
print(lanche[1:3])#mostra do elemento 1 até o 3 e descarta o terceiro elemento
print(lanche[2:])#mostra do elemento 2 até o final
print(lanche[:2])#mostra do primeiro elemento até o 2 elemento
#tuplas são imutaveis. não se atribui valores na tupla a não ser na declaração dela
for comida in lanche:
    print(f" eu vou comer {comida}")
print("comi pra caramba!")

for cont in range (0, len(lanche)): #mostra a posicão do elemento
    print(f'eu vou comer{lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f"eu vou comer ")

print(sorted(lanche))#mostra em ordem os elementos

for t in times:#ostra uma lista com os elementos da tupla
    print(times)
print(f"o valor 3 apareceu na {num.index(3)} posição") #mostra a posição