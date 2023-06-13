frase = str(input('Escreva sua frase: ')) .strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
