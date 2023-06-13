numextenso = ('zero', 'um', 'dois', 'três', 'quatro',
              'cinco', 'seis', 'sete', 'oito',
              'nove', 'dez', 'onze', 'doze', 'treze',
              'catorze', 'quinze', 'dezesseis', 'dezessete',
              'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Número inválido! Tente novamente')
print(f'Você digitou o número {numextenso[numero]}')

