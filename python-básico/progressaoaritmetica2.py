termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont += 1


