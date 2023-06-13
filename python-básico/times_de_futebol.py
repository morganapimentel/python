times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('=' *30)
print(f'Os 5 primeiros times são:\n{times[:6]}')
print('=' *30)
print(f'Os 4 últimos times colocados são: \n{times[-4:]}')
print('=' *30)
print(f'Times em ordem alfabética: \n{sorted(times)}')
print('=' *30)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')