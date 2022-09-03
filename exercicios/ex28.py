'''
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
'''
from random import randint # Importa números aleatórios.
from time import sleep # Importa um temporizador
computador = randint(0, 5) # Faz o computador sortear um número.
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print(f'Ganhei, eu pensei no número {computador} e não no número {jogador}')
