km = float(input('Informe o percurso percorrido em KM: '))
dias = int(input('O carro ficou alugado por quantos dias? '))
diaria = dias * 60
percurso = km * 0.15
#valor_total = diaria + percurso
print('Valor a pagar:R$ {:.2f}' .format(diaria+percurso))
