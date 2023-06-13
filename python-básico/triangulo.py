#maior que a diferença e menor que a soma
a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))
if a < b + c and b < a + c and c < a + b:
    print('Sim, temos um triângulo!')
else:
    print('Não é possível formar um triângulo com esses valores.')