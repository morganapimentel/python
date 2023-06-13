import math
grau = float(input('Informe a medida o grau: '))
sen = math.sin(math.radians(grau))
coss = math.cos(math.radians(grau))
tg = math.tan(math.radians(grau))
print('O seno de {} mede: {:.1f}' .format(grau, sen))
print('O cosseno de {} mede: {:.1f}'.format(grau, coss))
print('A tangente de {} mede: {:.1f}' .format(grau, tg))
