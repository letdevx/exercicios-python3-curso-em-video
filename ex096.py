def calculador(l, c):
    print('-'*30)
    area = l * c
    print(f" A área de um terreno de {l}x{c} é {area}m") 


print("controle de terrenos") 
l = float(input("Largura (m): "))
c = float(input("COMPRIMENETO (m):")) 
calculador(l,c)
