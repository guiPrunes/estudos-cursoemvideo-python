# ANÁLISADOR DE NÚMEROS PRIMOS

num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1): #1 - número digitado
    if num % c == 0: #resto da divisão inteira for 0
        print('\33[32m', end='')# dá cor
        cont += 1#conta quantos deram 0
    else:
        print('\33[31m', end='')#dá cor
    print(f'{c}', end=' ') #mostra os números do for
if cont == 2: # se tiver duas divisões
    print(f'\n\033[mO número foi divisivel {cont} vezes.')
    print(f'\033[34mO número {num} é primo.')
else: # se tiver mais que duas
    print(f'\n\033[mO número foi divisivel {cont} vezes.')
    print(f'\033[34mO número {num} não é primo.')