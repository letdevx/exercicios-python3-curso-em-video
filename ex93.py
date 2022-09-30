jogador = {} 
partidas = []
totalGols = 0

jogador["nome"] = str(input("digite o nome do jogador: ")) 
jogador["numeroPartidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou: "))

for cont in range (0,jogador["numeroPartidas"]):
    jogador.append = int(input(f"Quantos gols na partida {cont}: "))
    jogador["numeroGols"]= partidas[:]
    totalGols += jogador["numeroGols"] 
jogador["total"] = totalGols

print("-=" * 30)
print(jogador)

print("-=" * 30)
for k, v in jogador.items():
    print(f" {k} {v} ") 

print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {jogador['numeroPartidas']} partidas")

for i, v in enumerate (jogador['numeroGols']):
    print(f" => na primeira partida {i} fez {v} gols")
print(jogador['total'])
