# EXERCÍCIO DE DICIONÁRIOS APRIMORADO

dici = dict()
lista_gols = list()
princ = list()

while True:
    dici['nome'] = str(input('Nome do jogador: '))
    part = int(input('Nº de partidas: '))
    for c in range(0, part):
        lista_gols.append(int(input(f'  Nº de gols na partida {c}: ')))
    dici['gols'] = lista_gols[:]
    dici['total'] = sum(lista_gols)
    princ.append(dici.copy())
    lista_gols.clear()
    cont = str(input('Continuar? [S/N]: ')).upper()[0]
    while not cont in 'SN':
        print('Resposta inválida, tente novamente...')
        cont = str(input('Continuar? [S/N]: ')).upper()[0]
    if cont == 'N':
        break

print('=' * 30)
print('cód.', end=' ')
for v in dici.keys():
    print(f'{v:<15}', end='')
print()

for k, v in enumerate(princ):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

# for c in range(0, len(princ)):
#   print(f'c:>3}', end=' ')
#   for v in princ[c].values():
#       print(f'{str(v):<15}, end=' ')
# print()

print('=' * 30)
dados = int(input('Mostrar dados de qual jogador? '))
while not dados == 999:
    if dados > len(princ) - 1:
        print('Não há jogadores registrados neste código. Tente novamente...')
        dados = int(input('Mostrar dados de qual jogador? '))
    elif dados <= len(princ) - 1:
        print('=' * 30)
        print(f'{'LEVANTAMENTO DE DADOS':^30}')
        print(f'{'JOGADOR:'} {princ[dados]["nome"]}')
        for c, v in enumerate(princ[dados]["gols"]):
            print(f'    No jogo {c} fez {v} gols')
        print('=' * 30)
        dados = int(input("Mostrar dados de qual jogador?: "))
print(f'Fechando o programa...volte sempre!')