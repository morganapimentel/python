print('='*30)
print('CADASTRO DE PESSOAS')
print('='*30)
cont18 = conthomem = contmulher20 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('SEXO: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if sexo in 'M':
        conthomem += 1
    if sexo in 'F':
        if idade < 20:
            contmulher20 += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}  \nTotal de homens cadastrados: {conthomem}  \nTotal de mulheres com menos de 20 anos: {contmulher20}')
