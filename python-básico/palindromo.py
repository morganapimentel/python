frase = str(input('Digite uma palavra ou frase: ')) .strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1 ,-1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('As palavras formam um palíndromo!')
else:
    print('As palavras não formam um palíndromo!')