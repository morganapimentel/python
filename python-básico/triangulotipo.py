lado1 = float(input('Digite o valor do lado 1: '))
lado2 = float(input('Digite o valor do lado 2: '))
lado3 = float(input('Digite o valor do lado 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os lados formam um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Esses valores NÃO formam um triângulo')
