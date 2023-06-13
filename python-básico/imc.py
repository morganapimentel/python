peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/(altura * altura)
print('Seu IMC é {:.1f} '.format(imc), end='')
if imc < 18.5:
    print('e você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('e você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('e você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('e você está com obesidade!')
elif imc >= 40:
    print('e você está com obesidade mórbida!')