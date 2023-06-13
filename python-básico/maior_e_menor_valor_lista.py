valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor da {cont +1}ª posição: ')))
print(f'Os valores digitados foram: {valores}')
print(f'O menor valor digitado foi {min(valores)} e está na posição: ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p+1}...', end='')
print()
print(f'O maior valor digitado foi {max(valores)} e está na posição: ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p+1}...', end='')
print()