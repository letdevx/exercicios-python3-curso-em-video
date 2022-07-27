# Listas - listas são mutaveis
lanche []
lanche.append("bolo") #adiciona um elemento na lista
lanche.insert(0, "cachoro quente") #insere um elemento na posição selecionada
del lanche [3]
lanche.pop(3)#elimina o elemento selecionado pode ser usasdo pra eliminar o utimo elemento
lanche.remove("pizza")#elimina o elemnto e reposicona a contagem dos indices
lanche.pop #elimina o utimo elemento
num.remove(2) #elimimina o primeiro num 2

if'pizza'in lanche:
    lanche.remove("pizza") #remove o elemento selecionado se ele existir

valores1= list(range(4,11)) #cria uma lisata usando esse intervalo

num = [2,5,9,1]
num[2] = 3 #subistitui o 2 pelo 3
num.append(7)#adiciona p elemento 7 a lista)
num.sort(reverse=True)       #coloca os elementos em ordem reversa
num.insert(2,0)
print(num)

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate (valores):
     print(f"na posição {c} envontei o valor {v}!")
print("cheguie ao final da lista")

for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

a = [2, 0, 0, 6, 0]
b = a[:] cria uma copia dos valores