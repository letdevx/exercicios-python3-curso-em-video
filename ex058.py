import random
from time import sleep
print('--=' * 50)
print(''' Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
sera que você consegue adivinahr qual foi?
''')
print('--=' * 50)
sorteio = random.randint(0, 11)
num = int(input("Qual o seu palpite? "))
palpite = 0
while (sorteio != num):
     if num > sorteio:
        print("Menos...Tente mais uma vez")
        num = int(input("qual o seu palpite? "))
        palpite += 1
     if num < sorteio:
        print("Mais... tente mais uma vez")
        num = int(input("qual o seu palpite ? "))
print("Acertou com {} tentativas parabéns!".format(palpite))