cadastro = dict()
galera = list()
contador = 0
contmedia = 0
contidade = contfem = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    contador += 1
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
        if cadastro['sexo'] == 'F':
            contfem += 1
    cadastro['idade'] = int(input('Idade: '))
    contidade += 1
    contmedia += cadastro['idade']
    media = contmedia / contidade
    galera.append(cadastro.copy())
    while True:
        resposta = str(input('Quer continuar? S/N: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'A)Foram cadastradas {contador} pessoas.')#pode usar o len(galera) pra ver a qtd de pessoas cadastradas
print(f'B)A média de idade é de {media:.0f} anos.')
print('C)As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end='/')
    #else:
        #print('C)Nenhuma mulher foi cadastrada.') Não entendi pq ele repete a frase
print()
print('D)Lista das pessoas que estão acima da média: ')
for c in galera:
    if c['idade'] > media:
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};')



