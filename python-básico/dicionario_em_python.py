ficha = dict()
resultado = ''
ficha['nome'] = str(input('Nome do aluno: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
print(f'O nome é igual a {ficha["nome"]}\nA média é igual a {ficha["media"]}')
if ficha['media'] >= 7.0:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'
print(f'E o resultado é {resultado}')
