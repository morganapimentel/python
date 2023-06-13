def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    :param n: número a ser fatorado
    :param show: opcional que mostra o cálculo
    :return: retorna o valor do fatorial do número n
    """
    multiplicador = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        multiplicador *= c
    return multiplicador


#print(fatorial(5, show=True))
help(fatorial)
