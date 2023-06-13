velo = float(input('Infome a sua velocidade em KM/H: '))
multa = (velo % 80.0) * 7.0
if velo > 80.0:
    print('Você foi multado em R${} '. format(multa))
else:
    print('Você não foi multado')
print('Tenha um bom dia e dirija com cuidado!')