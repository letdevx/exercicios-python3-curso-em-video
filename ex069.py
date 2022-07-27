idademaior = 0
sexo_masculino = 0
mulher_menor = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input("Idade:"))
    sexo = " "
    while sexo not in "MF":
        sexo = (input("Sexo [M/F]")).strip().upper()[0]

    if idade >= 18:
        idademaior += 1
    if sexo == "M":
        sexo_masculino += 1
    if idade < 20 and sexo == "M":
        mulher_menor += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar ? [S/N]")).strip().upper()[0]

    if opcao == "N":
        break

print(f"O total de pessoas com mais de 18 anos é {idademaior}")
print(f"Temos {sexo_masculino} homens cadastrados")
print(f"e temos {mulher_menor} mulheres com menos de 20 anos")