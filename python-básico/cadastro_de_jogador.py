cadastro = dict()
gols = list()
cont = 1
total = 0
cadastro['nome'] = str(input('Nome do jogador: '))
partida = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
while cont <= partida:#pode ser um for c in range(0, partida)
    gols.append(int(input(f'Quantos gols na partida {cont}? ')))
    cont += 1
cadastro['gols'] = gols[:]
for g in gols:
    total = total + g
    cadastro['total'] = total #pode ser tb cadastro[total] = sum(gols)
print('-=' * 30)
print(cadastro)
for k, v in cadastro.items():
    print(f'o campo {k} tem valor {v}')
print('-=' *30)
print(f'O jogador {cadastro["nome"]} jogou {partida} partidas: ')
for c, v in enumerate(gols):
    print(f'  => Na partida {c+1} fez {v} gols')
print(f'Foi um total de {total} gols!')
