a = int(input("Primeiro valor "))
b = int(input("segundo valor "))
opcao = 0
while (opcao != 5):
   print("[1] somar")
   print("[2] multiplicar")
   print("[3] maior")
   print("[4] novos numeros]")
   print("[5] sair do programa")
   opcao =int(input(">>>>>> Qual é su opção?"))
   print("===============================================")
   if opcao == 1:
     soma = a + b
     print("A soma entre {} e {} é: {} ".format(a, b, soma))
   elif opcao == 2:
      multiplica = a * b
      print("A multiplicação entre {} e {} é: {}".format(a, b, multiplica))
   elif opcao == 3:
      if a > b:
         maior = a
      else:
         maior = b
         print("Entre {} e {} o maior é {}".format(a, b, maior))
   elif opcao == 4:
      print("informe os números novamente:")
      a = int(input("Primeiro valor "))
      b = int(input("segundo valor "))
   elif opcao == 5:
      print("Finalizando")
   else:
      print("opção invalida")