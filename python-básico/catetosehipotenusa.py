import math
b = float(input('Digite a medida do lado oposto do triângulo: '))
c =float(input('Digite a medida do lado adjacente do triângulo: '))
#hipo = math.sqrt(b*b + c*c)pode ser dessa forma também
hipo = math.hypot(b,c)
print('O valor da hipotenusa é: {}' .format(hipo))
