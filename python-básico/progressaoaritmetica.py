termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
decimo = termo + (10 -1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' ')