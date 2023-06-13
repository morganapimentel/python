from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores na lista:')
    sleep(1)
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        sleep(0.5)
        print(f'{n},', end=' ')
    print('PRONTO!')


def somaPar(lista):
    somapares = 0
    for valor in lista:
        if valor % 2 == 0:
            somapares += valor
    print(f'Somando os valores pares entre {lista} temos o valor: {somapares} ')


numeros = list()
sorteia(numeros)
somaPar(numeros)

