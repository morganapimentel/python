distancia = float(input('informe a distância da viagem: '))
if distancia <=200:
    print('A passagem custará {}' .format(distancia * 0.50))
else:
    print('A passagem custará {}' .format(distancia * 0.45))

    #if simplificado: preco = distancia * 0.50 if distancia<=200 else distancia * 0.45

