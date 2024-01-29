# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
soma = 0

while True:
        try:
            n1 = int(input("Digite um número: "))
        except:
            print('Digite números inteiros')
            continue

        try:
            n2 = int(input("Digite outro número: "))
        except:
            print('Digite números inteiros')
            continue
        
        for i in range(n1 + 1, n2):
            print(i)
        for i in range(n2 + 1, n1):
            print(i)

        soma = n1 + n2
        print(f'A soma dos númeors é {soma}')
                

# n1 = int(input("Digite um número: "))     Gabarito original
# n2 = int(input("Digite outro número: "))

# for i in range(n1 + 1, n2):
#         print(i)
# for i in range(n2 + 1, n1):
#         print(i)




# num1 = 0
# num1_int = 0
# num2 = 0
# num2_int = 0
# num_inter = 0

# while True:
#     if num1 == 0:
#         input('Digite um número inteiro: ').isdigit()
#         num1_int = int(num1)
#     else:
#         print('Digite apenas números inteiros').isdigit()
#         continue

#     if num2 == 0:
#         input('Digite outro número inteiro: ')
#         num2_int = int(num2)
#     else:
#         print('Digite apenas números inteiros')
#         continue

#     num_inter = num1_int 
    

#     break