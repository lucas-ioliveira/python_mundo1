'''
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''
import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a tângente de {tangente:.2f}')