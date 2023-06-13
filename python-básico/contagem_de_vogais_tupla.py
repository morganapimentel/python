palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR')
for nome in palavras:
    print(f'\nNa palavra {nome} temos as vogais: ', end='')
    for letra in nome:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')