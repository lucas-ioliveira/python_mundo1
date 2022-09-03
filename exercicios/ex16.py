'''
Crie um programa que leia um número real
qualquer pelo teclado e mostre na tela
a sua porção inteira.
'''
import math
n = float(input('Digite um número real: '))
ni = math.trunc(n)
print(f'O número {n} tem a parte inteira {ni}')