num = 0 #num = cont = soma = 0 (outra maneira de fazer)
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 pra parar]: '))
    cont += 1
    soma += num
    if num == 999:
        cont = cont -1
        soma = soma - 999
print('Você digitou {} números e a soma deles foi {}'.format(cont, soma))
