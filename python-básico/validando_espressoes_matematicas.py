cont1 = cont2 = 0
expressao =str(input('Digite a expressão: '))
for simbolo in expressao:
    if simbolo == '(':
        cont1 += 1
    elif simbolo == ')':
        cont2 += 1
if cont1 == cont2:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')

