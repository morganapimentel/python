dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso em Kg: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
for c in pessoas:
    if c[1] == maior:
        print(f'O maior peso cadastrado foi o de {c[0]} no valor de {maior}Kg')
    if c[1] == menor:
        print(f'O menor peso cadastrado foi o de {c[0]} no valor de {menor}Kg')



