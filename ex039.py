# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

atual = date.today().year
anos_nas = int(input("Digite o seu ano de nascimento"))
idade = atual - anos_nas
anos_alistamento = anos_nas + 18
anos_falta =  anos_alistamento - atual
anos_pasados = atual - anos_alistamento

if idade < 18:
    print("Ainda faltam {} anos para o seu alistamento que sera no ano de {}".format(anos_falta, anos_alistamento))

elif idade > 18:
    print("A data do seu alistamento já passou a {} anos, seu ano de alistamento foi {}".format(anos_pasados,anos_alistamento))

else:
    print("Alistece imediatamente")