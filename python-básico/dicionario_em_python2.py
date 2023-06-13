ficha = dict()
ficha['nome'] = str(input('Nome do aluno: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['media'] >= 7.0:
    ficha['resultado'] = 'Aprovado'
elif ficha['media'] <= 5 and ficha['media'] < 7:
    ficha['resultado'] = 'Recuperação'
else:
    ficha['resultado'] = 'Reprovado'
for k, v in ficha.items():
    print(f' {k} é igual a {v}')

