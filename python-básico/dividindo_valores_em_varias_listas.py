lista1 = []
listapar =[]
listaimpar = []
while True:
    n = lista1.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?(S/N): ')).strip().upper()
    if resp in 'N':
        break
for v in lista1:
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)
print(f'A lista completa é {lista1}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpar é {listaimpar}')