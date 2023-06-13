nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('\033[36mParabéns, sua média foi {:.1f} e você passou de ano!' .format(media))
elif media >= 5 and media <= 6.9:
    print('\033[33mSua média foi {:.1f} e você está na recuperação!' .format(media))
elif media < 5:
    print('\033[31mSua média foi {:.1f} e você não passou de ano!'.format(media))
