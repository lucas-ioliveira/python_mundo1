'''
Cores no terminal
Padrão ANSI
representação: ex \033[0:33:44m
códigos para style:
0- nome
1- bold
4-underline
7-negative
códigos para text:
30-branco
31-vermelho
32-verde
33-amarelo
34-azul
35-roxo
36-ciano
37-cinza
códigos para background:
40-branco
41-vermelho
42-verde
43-amarelo
44-azul
55-roxo
46-ciano
47-cinza
'''
# Exemplo:
print('\033[4;30;45mOlá, mundo!\033[m')

