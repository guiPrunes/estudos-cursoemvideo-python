# MATRIZ 

matriz = [0,0,0],[0,0,0],[0,0,0]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[coluna][linha] = int(input(f'[{linha}, {coluna}] '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[c][l]}]', end=' ')
    print()