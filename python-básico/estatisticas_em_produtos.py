print('{:=^40}'.format(' LOJÃO TEM DE TUDO '))
totcompra = prodmaismil = cont = 0
barato = ' '
while True:
    prod = str(input('NOME DO PRODUTO: '))
    preco = float(input('PREÇO R$: '))
    cont += 1
    continuar = ' '
    totcompra += preco
    while continuar not in 'SN':
        continuar = str(input('Quer adicionar mais produtos? S/N: ')).strip().upper()[0]
    if preco > 1000:
        prodmaismil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    if continuar == 'N':
        break
print(f'Valor total da compra: R$ {totcompra:.2f}')
print(f'Total de produtos com valor acima de R$1000: {prodmaismil}')
print(f'O produto de menor valor foi {barato} e custou R$ {menor:.2f}')

