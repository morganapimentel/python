from random import randint
print('='*30)
print('Vamos jogar Par ou Ímpar?')
print('='*30)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    computador = randint(0,10)
    soma = n + computador
    pop = ' '
    while pop not in 'PI':
        pop = str(input('Par ou Ímpar? [P ou I]: ')).upper()[0].strip()
    if pop == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {n} e computador {computador}\nTotal de {soma} deu PAR!\nVocê venceu!\nVamos jogar novamente...')
            cont += 1
        else:
            print(f'Você jogou {n} e computador {computador}\nTotal de {soma} deu ÍMPAR!\nVocê perdeu!\n')
            break
    elif pop == 'I':
        if soma % 2 == 1:
            print(f'Você jogou {n} e computador {computador}\nTotal de {soma} deu ÍMPAR!\nVocê venceu!\nVamos jogar novamente...')
            cont += 1
        else:
            print(f'Você jogou {n} e computador {computador}\nTotal de {soma} deu PAR!\nVocê perdeu!\n')
            break
print(f'O total de vezes que você ganhou foi {cont}')