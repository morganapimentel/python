num = int(input('Digite um número: '))
cont = 0
soma = 0
maior = menor = 0
while num != 0:
    num = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    soma = soma + num
    num = int(input('Digite um número: '))
    media = soma / cont
print('Foram digitados {} valores e a soma foi {}'.format(cont, soma))
print('O maior valor lido foi {} e o menor foi {}'.format(maior, menor))
print('FIM')