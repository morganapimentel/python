cadastro = []
boletim = []
notas = []
while True:
    cadastro.append(str(input('Digite o nome do aluno: ')))
    for n in range(0, 2):
        notas.append(float(input(f'Informe a {n+1}ª nota: ')))
    notas.append(cadastro[:])
    #cadastro.clear()
    resposta = str(input('Quer continuar?[S/N]: '))
    if resposta in 'Nn':
        break
    for p in notas:
        media = notas[0] + notas[1] / 2
print(notas)
print(media)
