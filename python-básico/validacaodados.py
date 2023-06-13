sexo = str(input('Informe o sexo (M/F): ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Informe novamente o sexo (M/F): ')).strip().upper()[0]
print('O sexo {} foi recebido com sucesso!'.format(sexo))
