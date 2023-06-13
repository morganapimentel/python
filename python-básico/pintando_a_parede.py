altura = float(input('Informe o valor da altura em metros: '))
largura = float(input('Informe o valor da largura em metros: '))
area = altura * largura
tinta = area / 2
print('A área total a ser pintada mede {:.2f} m2 e precisa de {:.2f}l de tinta'.format(area, tinta))
