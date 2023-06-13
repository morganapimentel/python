from datetime import date
maior = 0
menor = 0
for ano in range(1, 8):
    nasc = int(input('Qual sua data de nascimento? '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Pessoas que atingiram a maioridade: {} \nPessoas que não atingiram a maioridade: {}'.format(maior, menor))
