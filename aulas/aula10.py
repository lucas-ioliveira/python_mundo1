'''
Aula sobre estruturas condicionais
if,else
'''
#ex
'''
nome = str(input('Digite seu nome: '))
if nome == 'lucas':
    print(f'Que nome lindo você tem.')
else:
    print('Seu nome é tão normal')
print(f'Bom dia, {nome}!')
'''
#ex2
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2) / 2
print(f'A sua média é: {m}')
if m >= 6.0:
    print('A sua média foi boa, PARABÉNS!')
else:
    print('A sua média foi ruim, ESTUDE MAIS!')