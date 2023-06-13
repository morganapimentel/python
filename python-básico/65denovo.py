resp = 'S'
cont = 0
soma = 0
maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0].upper()
    cont += 1
    soma = soma + num
    media = soma / cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Soma {} \ncont {} \nmédia {} \nmenor {} \nmaior {} '.format(soma, cont, media, menor, maior))