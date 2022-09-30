from time import sleep

def maiorValor(*num):
    maiorv = 0
    print('-*'*30) 
    print("analisando valores")
    print(f" os valores digitados foram {num} {len(num)}valores ao todo")
    for i, valor in enumerate(num):
        if valor[0] > maiorv:
            maiorv = valor 
    print (f" maior valor informado foi{maiorv}") 
   
    print('-*'*30) 


valores = (1,2,3,4,5)
maiorValor(valores)

