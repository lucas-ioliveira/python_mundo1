'''
Manipulando cadeia de texto.
'''
# exemplos
frase = 'Curso em Vídeo Python'
frase2 = 'Aprenda Python'
print(f'Essa frase tem {len(frase)} caracteres.')
print(frase[9:13])
print(frase.count('o'))
print(frase.find('Vídeo'))
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
#
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

#
print(frase.split())
print('-'.join(frase))