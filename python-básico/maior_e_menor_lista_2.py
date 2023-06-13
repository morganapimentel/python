valores = list()
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor para a {cont+1}ª posição: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Os valores digitados foram: {valores}')
print(f'O menor valor digitado foi {menor} e está na posição: ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p + 1}...', end='')
print()
print(f'O maior valor digitado foi {maior} e está na posição: ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p+1}...', end='')
print()