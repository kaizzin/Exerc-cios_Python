'''
Verificar se uma palavra é um palíndromo: Implemente um programa que verifica se uma
palavra é um palíndromo. Um palíndromo é uma palavra que pode ser lida da mesma
forma tanto da esquerda para a direita quanto da direita para a esquerda.

'''

palavra = input('Digite uma palavra: ')

if palavra == palavra[::-1]:
    print(f'{palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palíndromo')