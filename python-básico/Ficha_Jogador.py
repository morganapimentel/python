def ficha(nome='<desconhecido>', gols='0'):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato. '



jogador = str(input('Nome do jogador: '))
num_gols = str(input(f'Quantos gols o jogador {jogador} fez? '))
print(ficha(jogador, num_gols))

