nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo: {}' .format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('O nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} ' .format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))