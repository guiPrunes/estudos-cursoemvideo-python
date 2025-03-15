# MATRIZ E SOMA DE COLUNAS/LINHAS

matriz = [0,0,0],[0,0,0],[0,0,0]
pares = soma = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[coluna][linha] = int(input(f'[{linha}, {coluna}] '))
        if matriz[coluna][linha] % 2 == 0:
            pares += matriz[coluna][linha]
print ()
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[coluna][linha]:^5}]', end=' ')
    print()
print()
print(f'A SOMA DOS VALORES PARES É: {pares}.')
for coluna in range(0,3):
    soma += matriz[2][coluna]
print(f'A SOMA DOS VALORES DA 3ª COLUNA É: {soma}.')
for linha in range(0,3):
    if linha == 0:
        maior = matriz[linha][1]
    else:
        if matriz[linha][1] >= maior:
            maior = matriz[linha][1]
        else:
            menor = matriz[linha][1]
print(f'O MAIOR VALOR DA 2ª LINHA É: {maior}.')