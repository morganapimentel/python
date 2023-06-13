def leiaInt(name):
    ok = False
    val = 0
    while True:
        n = str(input(name))#Não entendi por que tem que criar essa variável
        if name.isnumeric():
            val = int(name)
            ok = True
        else:
            print('ERRO!Digite um número inteiro válido')
        if ok:
            break
    return val


#n = str(input('Digite um número:'))
valor = leiaInt('Digite um número: ')
print(f'Você digitou o número {valor}')


