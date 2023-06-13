valores = list()
while True:
    n = int(input('Digite um número:'))#Não entendi como o n entra na lista
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!Não será adicionado!')
    continuar = str(input('Deseja inserir mais um número? (S ou N)? ')).upper().strip()
    if continuar in 'N':
        break
valores.sort()#Não entendi pq ficou aqui e não nas chaves embaixo
print(f'Os valores digitados foram: {valores}')