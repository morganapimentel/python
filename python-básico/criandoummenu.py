from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('-----Selecione uma das opções abaixo-----')
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('Informe a opção escolhida: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('{} x {} = {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        if n1 < n2:
            maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        else:
            print('Os números são iguais!')
    elif opcao == 4:
        print('Informe dois números novamente:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Saindo...')
        sleep(1)
    else:
        print('Dados inválidos!Tente novamente.')
    sleep(2)
print('Fim do programa!Até mais!')



