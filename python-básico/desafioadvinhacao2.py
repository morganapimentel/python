from time import sleep
from random import randint
tentativas = 1
computador = randint(0, 10)
jogador = int(input('Em qual número eu pensei? '))
while computador != jogador:
    if computador > jogador:
        jogador = int(input('Meu número é maior!Tente novamente: '))
    if computador < jogador:
        jogador = int(input('Meu número é menor!Tente novamente: '))
    tentativas += 1
print('PROCESSANDO...')
sleep(1)
print('Você acertou!O número que pensei foi {} e você conseguiu na {}ª tentativa! '.format(jogador, tentativas))