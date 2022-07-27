#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
print("-="*50)
print("Analisador de Triângulos")
print("-="*50)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 +r3 and r2< r1 +r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo!")
    if r1 == r2 and r1 == r3:
        print("equilatero")
    elif r1 == r2 and r1 != r3:
        print("isoceles")
    else:
        print("escaleno")
else:
    print("Os triângulos acima não podem formar um triângulo!")