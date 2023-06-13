from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - ano
cadastro['ctps'] = int(input('Carteira de Trabalho(digite 0 se não tiver): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - ano
for k, v in cadastro.items():
    print(f'{k} tem o valor {v} ')
