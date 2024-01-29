'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''
# nome=str(input("informe um nome--> "))
# while ( len(nome) <=  3 ):
# 	nome=str(input("informe um nome--> "))

# #Idade: entre 0 e 150;

# idade=int(input("informe a idade--> "))
# while ( idade > 150 or idade < 0 ):
# 	idade=int(input("informe a idade--> "))
	
	
# #Salário: maior que zero;
# salario=float(input("informe um salário--> "))
# while ( salario < 0 ):
# 	salario=float(input("informe um salário--> "))
	
# #Sexo: 'f' ou 'm';

# sexo=str(input("informe a inicial do seu sexo--> "))
# while  sexo !="f" and sexo!="m" :
# 	sexo=str(input("informe a inicial do seu sexo--> "))
	
# #Estado Civil: 's', 'c', 'v', 'd';

# estado_civil=str(input("informe a inicial do seu estado civil-->"))
# while ( estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" ):
# 	estado_civil=str(input("informe a inicial do seu estado civil-->"))


import os

nome = ''
idade = 0
idada_float = 0
salario = 0
salario_float = 0
sexo = ''
sexo_str = ''
sexo_fem = 'f'
sexo_masc = 'm'
estado_civil = 's', 'c', 'v', 'd'

while True:
    nome = input('Digite seu nome: ')
    if len(nome) <= 3:
        print('Informe no mínimo 4 letras')
        continue

    idade = input('Digite sua idade: ')
    try:
        idade_float = float(idade)
        if idade_float < 0 or idade_float > 150:
            print('A idade deve estar entre 0 e 150 anos')
            continue
    except:
        print('Por favor, informe apenas números')
        continue
    
    salario = input('Informe seu salário: ')
    try:
        salario_float = float(salario)
        if salario_float <= 0:
            print('O sálario precisa ser maior que 0')
            continue
    except:
        print('Informe apenas números')
        continue

    sexo = input('Qual o seu sexo (f)eminino ou (m)asculino: ').isalpha()
    try:
        sexo_str = sexo
        if sexo_str not in sexo_fem or sexo_str not in sexo_masc:
            print('Informe com "f" para feminino e "m" para masculino')
        continue 
    except:
        print('Informe apenas letras.')
        continue

    

    

   
    
    
