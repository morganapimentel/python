numeros = []
resposta = ' '
while True:
    n = numeros.append(int(input('Digite um número: ')))
    while resposta not in 'NS':
        resposta = str(input('Quer continuar?(S/N): ')).upper().strip()
    if resposta in 'N':
        break
print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente foi {numeros}.')
if 5 in numeros:
    print('O número 5 apareceu na lista!')
else:
    print('O número 5 não apareceu na lista!')
