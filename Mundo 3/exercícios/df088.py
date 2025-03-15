# JOGO DA MEGA SENA

from random import randint
from time import sleep

print(f'{' JOGO DA MEGA-SENA ':=^40}')
mega = []
jogos = []
njogos = int(input(f'Quantos jogos seram sorteados? >> '))
for j in range(0,njogos):
    while not len(jogos) == 6:
        n = randint(1,60)
        if n not in jogos:
            jogos.append(n)
    mega.append(jogos[:])
    jogos.clear()
for s in range(0, len(mega)):
    mega[s].sort()
    print(f'JOGO {s+1}: {mega[s]}')
    sleep(0.7)
print(f'{' BOA SORTE ':=^40}')
