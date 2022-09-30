
def contador (inicio, meio, fim):
    print(f"inicio {inicio} meio{meio} fim {fim}")
    for list in range(inicio, fim+1, meio):
        print(list)
    
    



contador(1, 1, 10)
contador(10, -2, 0) 

print("agora é sua vez digite: ")
inicio= int(input(" inicio"))
meio= int (input("meio: "))
fim= int(input("fim"))



