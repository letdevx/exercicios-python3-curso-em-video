# 6- crie um algoritimo que leia um número e mostre seu dobro,
# seu triplo e a raiz quadrada.
from typing import Union, Any

n = int(input("Digite um número: "))
dobro = n * 2
raiz_quadrada = n*n
triplo = n * 3
print("========================\nProcessando\n========================")
print(f"O número digitado é: {n}\nO dobro de {n} é: {dobro}\nA raiz quadrada de {n} é: {raiz_quadrada}\nO triplo de {n} é: {triplo}")
