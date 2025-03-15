# LISTAGEM DE PREÇOS TABULADA

listagem = ('Pão', 2, 'Salame', 22, 'Queijo', 6, 'Presunto', 7, 'Margarina', 4.50, 'Ovo', 14, 'Biscoto', 5, 'Trident', 2, 'Halls', 2, 'Café', 7.50)
print(f'{'':-^55}')
print(f'{'LISTAGEM DE PREÇOS':^55}')
print(f'{'':-^55}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<45}', end='')
    else:
        print(f'R$ {listagem[pos]:>6.2f}')
print(f'{'':-^55}')
    