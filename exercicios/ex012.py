'''
Faça um programa que leia o preço
de um produto e mostre seu novo preço,
com 5% de desconto.
'''
# Cálculo % - número * % /100
pp = float(input('Digite o preço do produto? R$ '))
np = pp - (pp * 5 / 100)
print(f'O preço do produto com 5% de desconto é: {np}')