# EXERCÍCIO PARES E IMPARES LISTA

princ = [[],[]]
for c in range(0,7):
    n = (int(input(f'Digite um número: ')))
    if n % 2 == 0:
        princ[0].append(n)
    if n % 2 == 1:
        princ[1].append(n)
princ[0].sort()
princ[1].sort()
print(f'*==*'*15)
print(f'NÚMEROS PARES: {princ[0]}')
print(f'IMPARES IMPARES: {princ[1]}')

