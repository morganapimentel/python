print('{:=^40}'.format(' LOJAS SOUZA '))
compra = float(input('Informe o valor da compra: R$ '))
print('''Como deseja pagar? Escolha as opções abaixo: 
[1] à vista dinheiro /cheque 
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão ''')
pagamento = int(input('Digite a opção escolhida: '))
if pagamento == 1:
    valor1 = compra * 0.90
    print('O valor final da sua compra é de R${}' .format(valor1))
elif pagamento == 2:
    valor2 = compra * 0.95
    print('O valor final da sua compra é de R${}'.format(valor2))
elif pagamento == 3:
    valor5 = compra /2
    print('O valor final da sua compra é de R${} dividido em 2x de R${}'.format(compra, valor5))
elif pagamento == 4:
    parcela = int(input('Em quantas parcelas? '))
    valor3 = compra + (compra * 0.2)
    valor4 = valor3 / parcela
    print('Sua compra será parcelada em {}X de {} com juros, e o valor final será de R${}'.format( parcela, valor4, valor3))
else:
    print('Por favor, escolha uma opção válida!')


