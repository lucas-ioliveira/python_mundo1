'''
Operadores aritméticos.
'''
# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Exponenciação **
# Divisão de inteiros //
# Mode %
# Raiz quadrada numero **(1/2)
# Raiz cubica numero ** (1/3)

'''
5 + 2
5 - 2
5 * 2
5 / 2
5 ** 2
5 // 2
5 % 2
81 ** (1/2)
25 ** (1/3)
'''
# Ex
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
print(f' A soma é {s}, a subtração é {sb}, o produto é {m}, a divião real é {d:.2f}')
print(f'A divisão inteira é {di}, o resto é {r}')
    