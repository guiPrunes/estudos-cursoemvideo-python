# ÍNDICE E POSIÇÃO NA LISTA

lista = []
for c in range(0,5):
    v = int(input('Digite um valor:'))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print('Adicionado ao final da lista...')
    else:
        posicao_do_indice = 0
        while posicao_do_indice < len(lista): #ou seja, menor que o número de elementos na lista
            if v <= lista[posicao_do_indice]:
                lista.insert(posicao_do_indice, v)
                print(f'Adicionado na posição {posicao_do_indice} da lista...')
                break
            posicao_do_indice += 1
    print(f'LISTA: {lista}')
    