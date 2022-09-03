'''
Escreva um programa que leia a velocidade de um carro, se ele
ultrapassar a velocidade de 80km/h, mostre uma mensagem que ele
foi multado, a multa custa R$7,00 por cada km acima do limite.
'''
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f} reais')
else:
    print('Tenha um bom dia, dirija com segurança!')