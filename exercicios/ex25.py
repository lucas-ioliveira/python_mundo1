'''
Crie um programa que leia o nome de uma pessoa e diga se
ela tem 'silva' no nome.
'''
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')