print("="*30)
print( "{:^30}" .format("BANCO CEV"))
print(("="*30))
nota_50 = 0
nota_10 = 0
nota_1 = 0
while True:
     saque = int(input("Qual valor você quer sacar? R$"))
     if saque/50 >=1:
         nota_50 = saque // 50
         saque -= nota_50 * 50
         print(f"total de {nota_50} cedulas de R$50")
     if saque / 20 >=1:
         nota_20 = saque // 20
         saque -= nota_20 *20
         print(f"total de {nota_20} cedulas de R$20")
     if saque / 10 >= 1:
         nota_10 = saque // 10
         saque -= nota_10 * 10
         print(f"total de {nota_10} cedulas de R$10")
     if saque / 1 >= 1:
         nota_1 = saque
         saque -= nota_1
         print(f"total de {nota_1} cedulas de R$1")
     if saque == 0:
         break
print("="*30)
print("VOLTE SEMPRE AO BANCO CEV! TENHA UM EXELENTE DIA")