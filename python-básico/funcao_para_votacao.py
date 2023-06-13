from datetime import date #pode colocar dentro da função pra economizar memória


def votacao(num):
    idade = date.today().year - num
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade >= 16 and idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


ano = int(input('Em que ano você nasceu? '))
print(votacao(ano))
