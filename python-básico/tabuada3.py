num = 0
while True:
    num = int(input('Digite um valor pra ver a tabuada: '))
    if num < 0:
        break
    print('-' *36)
    for c in range(1, 11):
        print(f'{num} x {c} = {c*num}')
    print('-' *36)
print('Programa Tabuada encerrado!')


