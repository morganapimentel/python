salario = float(input('Informe seu salário: R$ '))
if salario > 1250.00:
    salario2 = salario + (salario * 0.10)
if salario <= 1250.00:
    salario2 = salario + (salario * 0.15)
print('O salário com aumento é: R${}' .format(salario2))
