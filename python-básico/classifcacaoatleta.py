from datetime import date
ano = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos' .format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Categoria SÊNIOR')
elif idade > 25:
    print('Categoria MASTER')