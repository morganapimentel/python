dados = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Os números digitados foram: {dados}')
print(f'O número 9 apareceu {dados.count(9)} vezes')
for n in dados:
    if n % 2 == 0:
        print(f'Os números pares digitados foram: {n}', end=' ')
print('Não foram digitados  números pares')
if 3 in dados:
    print(f'O número 3 apareceu na {dados.index(3) +1}ª posição')
else:
    print('O número 3 não foi digitado')

