ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar?[S/N]: '))
    if resposta in 'Nn':
        break
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, v, in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')
while True:
    print('-' * 35)
    resposta2 = int(input('Quer mostrar nota de qual aluno?[999 encerra] '))
    if resposta2 == 999:
        break
    if resposta2 <= len(ficha) - 1:
        print(f'Notas de {ficha[resposta2][0]} são {ficha[resposta2][1]} ')
print('Volte sempre!')
