#PROGRAMA QUE CALCULA A SOMA ENTRE TODOS OS NÚMEROS
#ÍMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM
#NO INTERVALO DE 1 ATÉ 500

soma = 0
cont = 0
for c in range(3, 500, 6):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A SOMA É IGUAL A: {soma}.')
print(f'O CONTADOR DEU: {cont}.')