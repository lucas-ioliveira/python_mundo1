'''
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo
e todas as informações possiveis
sobre ela.
'''
algo = input('Digite algo: ')
print('O tipo primitivo de sse valor é ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico ', algo.isalnum())
print('Está em maiúscula? ', algo.isupper())
print('Está em minúscula? ', algo.islower())
print('Está capitalizada? ', algo.istitle())


