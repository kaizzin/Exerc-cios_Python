'''
Converter temperatura de Celsius para Fahrenheit: Escreva um programa que converta
uma temperatura em graus Celsius para Fahrenheit. Isso envolve a aplicação da fórmula
correta de conversão.
'''

celsius = input('Digite a temperatura em celsius: ')

try:
    celsius_float = float(celsius)
    fahrenheit = (celsius_float * 1.8) + 32
    print(f'{celsius_float}°C é equivalente a {fahrenheit}°F')
except:
    print('Digite um valor válido')