# LISTA DE PARES E ÍMPARES

lista = []
while True:
    lista.append((int(input('Digite um número: '))))
#
    ask = str(input('Quer continuar? [S/N] ')).upper().strip()
    while ask not in "SN":
        ask = str(input('Quer continuar? [S/N] ')).upper().strip()
    if ask == "N":
        break
#
pares = []
impares = []
for i, v in enumerate(lista):
    if lista[i] % 2 == 0:
        pares.append(v)
    if lista[i] % 2 == 1:
        impares.append(v)
print(f'A LISTA COMPLETA É: {lista}')
print(f'LISTA DOS PARES: {pares}')
print(f'LISTA DOS IMPARES: {impares}')
#
