def notas(*n, sit=False):
    dicionario = dict()
    dicionario['Total '] = len(n)
    dicionario['Maior nota '] = max(n)
    dicionario['Menor nota'] = min(n)
    dicionario['Media'] = sum(n)/len(n)
    if sit:
        if dicionario['Media'] >= 7:
            dicionario['Situação: '] = 'Aprovado'
        elif dicionario['Media'] < 7:
            dicionario['Situação:'] = 'Em recuperação'
        else:
            dicionario['Situação: '] = 'Reprovado'
    return dicionario

resposta = notas(9.0, 10.0, 5.0)
print(resposta)





