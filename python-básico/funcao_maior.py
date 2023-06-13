from time import sleep

def maiorvalor(*num):
    print('Analisando os valores passados... ')
    sleep(1)
    print(num)
    sleep(0.5)
    print(f'Foram informados {len(num)} valores.')
    print(f'O maior valor informado foi {max(num)} ')
    print('-=' *20)


maiorvalor(2, 6, 9, 5, 4, 3)
maiorvalor(3, 6, 9, 4)
maiorvalor(6, 4)
