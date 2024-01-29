'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input('Digite uma letra: ')
vogais = 'a','e','i','o','u','A','E','I','O','U'



if len(letra) == 1:
    if letra.isalpha():
        if letra in vogais:
            print(f'"{letra}" é uma vogal')
        else:
            print(f'"{letra}" não é uma vogal')
    else:
        print('Digite apenas letras')
elif len(letra) > 1:
            print('Você digitou vários números')
else:
    print('Digite apenas uma letra')



    
