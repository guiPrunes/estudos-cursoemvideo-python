# PROGRESSÃO ARITMÉTICA

pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
rng = pt + (10 - 1) * r
for c in range(pt, rng, r):
    print(f'{c}', end=' - ')
print('Fim')
