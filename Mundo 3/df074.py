# NÚMEROS SORTEADOS, MAIOR E MENOR

from random import randint

numaleatorios = (randint(1,100), randint(1,100), randint(1,100), randint(1,100),randint(1,100))
ordem = sorted(numaleatorios)
maior = ordem[-1]
menor = ordem[0]
print(f'VALORES SORTEADOS: {numaleatorios}')
print(f'MAIOR VALOR SORTEADO: {maior}')
print(f'MENOR VALOR SORTEADO: {menor}')