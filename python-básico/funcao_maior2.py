from time import sleep
def maiorv(* num):
    print('-=' * 30)
    print('Analisando os valores informados...')
    cont = maior = 0
    for valor in num:
        sleep(0.4)
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if cont > valor:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores')
    print(f'O maior valor informado foi {maior}')


maiorv(2, 6, 9, 5, 4, 3)
maiorv(3, 6, 9, 4)
maiorv(6, 4)