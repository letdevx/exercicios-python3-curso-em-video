from datetime import datetime 

cadastro = {} 
cadastro["nome"] = str(input("Digite o seu nome: "))
ano_nascimento = int(input("Qual seu ano de nascimento? "))
cadastro["idade"] = datetime.now().year - ano_nascimento
cadastro["num_carteira_trabalho"] = int(input("Digite o número da carteira de trabalho ou 0 para náo tenho: "))
if cadastro["num_carteira_trabalho"] != 0:
        cadastro["ano_contratacao"] = int(input("Qual o ano da sua contratacao? "))
        cadastro["ano_aposentadoria"] = cadastro["ano_contratacao"] + 30
        cadastro["idade_aposentadoria"] = cadastro["idade"] + 30 
        cadastro["salario"] = float(input("qual o seu salário? ")) 


print(f"")
for k, v in cadastro.items():
    print( f"  => {k} tem o valor {v} " )