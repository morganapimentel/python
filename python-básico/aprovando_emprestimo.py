casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o valor do salário: R$ '))
tempo = int(input('Em quantos anos você pretende pagar? '))
taxa = salario * 0.30
prestacao = casa / (tempo *12)
if prestacao < taxa:
    print('\033[32mSeu financiamento foi aprovado. O valor da prestação é R${:.2f} em {} anos.\033[m ' .format(prestacao, tempo))
else:
    print('\033[31mSeu financiamento foi negado.\033[m')
    