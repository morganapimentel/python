somaidade = 0
homemmaisvelho = ''
maioridadehomem = 0
menorvintemulher = 0
for p in range(1, 5):
    print('------ {}ª pessoa ------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        homemmaisvelho = nome
        maioridadehomem = idade
    if sexo == 'M' and idade > maioridadehomem:
        homemmaisvelho = nome
        maioridadehomem = idade
    if sexo == 'F' and idade < 20:
        menorvintemulher += 1
mediaidade = somaidade / 4
print('A média de idade é de {:.0f} anos'.format(mediaidade))
print('O homem mais velho é {} e tem {} anos' .format(homemmaisvelho, maioridadehomem))
print('Existem {} mulheres com menos de 20 anos' .format(menorvintemulher))
