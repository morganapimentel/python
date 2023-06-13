cont = soma = 0
while True:
    num = int(input('Digite um número (999 para encerrar) : '))
    if num == 999:
        break
    cont += 1
    soma = soma + num
print(f'A soma dos {cont} valores foi {soma}')
