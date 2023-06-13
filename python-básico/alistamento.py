from datetime import date
#sexo = str(input('Informe o sexo: '))
nascimento = int(input('Informe o ano de nascimento: '))
idade = date.today().year - nascimento
if idade == 18:
    print('É hora de se alistar! ')
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar ' .format(18 - idade))
elif idade > 18:
    print('Você passou do prazo em {} anos.'.format(idade - 18))