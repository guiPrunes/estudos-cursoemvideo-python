# JOGO DE SORTEIO DE NÚMEROS

from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados: ')

dict = {}
ordem = []

for c in range(1,5):
    dict[f'jogador{c}'] = randint(1,6)

for k,v in dict.items():
    print(f'O {k} tirou {v}')
    sleep(0.8)

print('=-'*35)

ranking = {}
ranking = sorted(dict.items(), key=itemgetter(1), reverse=True)
for c in range(len(ranking)): # dá pra ser com enumerate
    print(f'{c + 1}º lugar: {ranking[c][0]} com {ranking[c][1]}')
    sleep(0.8)
 