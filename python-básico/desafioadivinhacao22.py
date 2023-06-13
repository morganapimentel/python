from time import sleep
from random import randint
computador = randint(0, 10)
print('---------Tente adivinhar qual número eu pensei entre 0 e 10---------- ')
acertou = False
palpites = 0
while not acertou:
        jogador = int(input('Qual é seu palpite? '))
        palpites += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Meu número é maior! ')
            elif jogador > computador:
                print('Meu número é menor!' )
print('PROCESSANDO...')
sleep(1)
print('Você acertou na {}ª tentativa!' .format(palpites))


