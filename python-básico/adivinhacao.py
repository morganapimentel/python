from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você ganhou!')
else:
    print('Você perdeu! Eu pensei no número {} e não no número {}' .format(computador, jogador))
