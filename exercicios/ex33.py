'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor digitado foi: {menor}.')
# Verificando o maior valor.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi: {maior}')