# EXERCÍCIO DE DICIONÁRIOS

princ = {}
gols = []
total = 0
princ['nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {princ["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Gols na partida nº {c}: ')))
princ['gols'] = gols #não vi necessidade da [:], mas deve usar
for c in gols:
    total += c # ele usou sum() para somar sem declarar variável
princ['total'] = total
print('=-=' * 25)
print(princ)
print('=-=' * 25)
for k, v in princ.items():
    print(f'O campo {k} tem valor {v}.')
print('=-=' * 25)
print(f'O jogador {princ["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'=> Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {total} gols.')