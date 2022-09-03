'''
Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode comprar.
'''
r = float(input('Digite quantos reis você tem:R$ '))
d = r / 3.17
print(f'Você tem R${r:.2f} reais e pode comprar ${d:.2f} dólares')