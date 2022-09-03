'''
Faça um programa que leia a largura
e a altura de uma parede em metros,
calcule a sua área e a quantidade de
tinta necessária para pintá-la,
sabendo que cada litro de tinta,
pinta uma área de 2m².
'''
l = float(input('Digite a largura: '))
al = float(input('Digite a altura: '))
ar = l * al
lt = ar / 2
print(f'A sua parede tem a dimenssão de {l} x {al} e sua área é de {ar} m².')
print(f'Você precisa de {lt} litros de tinta para pintar sua parede.')