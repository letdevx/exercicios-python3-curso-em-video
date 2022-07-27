sexo = " "
while( sexo not in 'mMfF'):
    sexo = str(input("INFORME O SEU SEXO [F/M]:")).strip().upper()[0]
    print("opcao invalida tente novamente")