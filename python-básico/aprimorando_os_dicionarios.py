cadastro = dict()
gols = list()
tudao = list()
cont = 1
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partida):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    tudao.append(cadastro.copy())
    while True:
        resposta = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Digite apenas S ou N!')
    if resposta == 'N':
        break#até aqui é o código para ler os dados dos jogadores
print('-' * 40)
print('cod ', end='')
for i in cadastro.keys():#aqui começa a análise dos dados
    print(f'{i:< 15}', end='')
print()
for k, v in enumerate(tudao):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')#não entendi pq tem esse str antes de (d)
    print()
print('-' * 40)
while True:
    mostra = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if mostra == 999:
        break
    if mostra >= len(tudao):
        print(f'Não existe jogador com o código {mostra}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {tudao[mostra]["nome"]}')
        for i, g in enumerate(tudao[mostra]['gols']):#mostrando o levantamento do jogador em cada partida
            print(f'Na partida {i+1} fez {g} gols')
    print('-'*40)
print('VOLTE SEMPRE!')


