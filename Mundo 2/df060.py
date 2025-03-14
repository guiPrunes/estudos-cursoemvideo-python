# FATORIAL

num = int(input('Digite um número: '))
cont = num #vai começar no número, com ctz
f = 1 #fator nulo do fatorial
while cont > 0: #contagem regressiva
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont #num = 5, fatorial = 1x5, diminui 1 do numero // fatorial = 5x1 = 5, fatorial 5x1x4 == 5x4, fatorial = 5x4x1x3 == 5x4x3, fatorial = 5x4x3x1x2 == 5x4x3x2, fatorial 5x4x3x2x1x1 == 5x4x3x2x1 que dá 120.
    cont -= 1
print(f'{f}')