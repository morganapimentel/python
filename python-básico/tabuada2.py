num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    resultado = num * c
    print('{} X {:2} = {}' .format(num, c, resultado))
