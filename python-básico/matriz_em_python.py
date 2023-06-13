matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]#Não entendi porque ele colocou dois for
somapar = soma = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
        soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
        if matriz[l][c] == 0:
            maior = matriz[1][0] = matriz[1][1] = matriz[1][2]
        else:
            if matriz[1][0] > maior:
                maior = matriz[1][0]
            if matriz[1][1] > maior:
                maior = matriz[1][1]
            if matriz[1][2] > maior:
                maior = matriz[1][2]
    print()
print(f'A soma dos valores pares digitados é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O valor maior da segunda linha é {maior}')



